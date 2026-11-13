#pragma once

#include <node_api.h>

#include <string>

namespace daisy::binding {

/**
 * Hashes a file on a libuv worker thread and settles a Promise on the JavaScript thread.
 * The job owns itself: it is deleted in onComplete.
 */
class HashFileJob {
 public:
  /** Starts the job and returns its Promise. */
  static napi_value start(napi_env env, std::string path);

 private:
  explicit HashFileJob(std::string path);
  static void onExecute(napi_env env, void* data);
  static void onComplete(napi_env env, napi_status status, void* data);

  std::string path_;
  std::string result_;
  std::string error_;
  napi_deferred deferred_ = nullptr;
  napi_async_work work_ = nullptr;
};

}  // namespace daisy::binding
