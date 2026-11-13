#include "HashFileJob.hpp"

#include <exception>
#include <memory>

#include "NapiSupport.hpp"
#include "daisy/FileHasher.hpp"

namespace daisy::binding {

HashFileJob::HashFileJob(std::string path) : path_(std::move(path)) {}

napi_value HashFileJob::start(napi_env env, std::string path) {
  auto job = std::unique_ptr<HashFileJob>(new HashFileJob(std::move(path)));
  napi_value promise = nullptr;
  Napi::check(env, napi_create_promise(env, &job->deferred_, &promise), "create promise");
  Napi::check(env,
              napi_create_async_work(env, nullptr, Napi::string(env, "daisy.hashFile"), &HashFileJob::onExecute,
                                     &HashFileJob::onComplete, job.get(), &job->work_),
              "create async work");
  Napi::check(env, napi_queue_async_work(env, job->work_), "queue async work");
  job.release();  // owned by the queued work until onComplete
  return promise;
}

void HashFileJob::onExecute(napi_env /*env*/, void* data) {
  auto* job = static_cast<HashFileJob*>(data);
  try {
    job->result_ = FileHasher().sha256Hex(job->path_);
  } catch (const std::exception& error) {
    job->error_ = error.what();
  }
}

void HashFileJob::onComplete(napi_env env, napi_status status, void* data) {
  std::unique_ptr<HashFileJob> job(static_cast<HashFileJob*>(data));
  if (status == napi_cancelled) job->error_ = "Hashing was cancelled";
  if (job->error_.empty()) {
    napi_resolve_deferred(env, job->deferred_, Napi::string(env, job->result_));
  } else {
    napi_value message = Napi::string(env, job->error_);
    napi_value code = Napi::string(env, "ERR_DAISY_NATIVE_IO");
    napi_value error = nullptr;
    napi_create_error(env, code, message, &error);
    napi_reject_deferred(env, job->deferred_, error);
  }
  napi_delete_async_work(env, job->work_);
}

}  // namespace daisy::binding
