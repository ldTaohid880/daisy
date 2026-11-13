// Entry point of daisy_native.node. JavaScript API (typed in packages/native/src/DaisyNativeAddon.ts):
//   version(): string
//   sha256(data: Uint8Array | string): string            (synchronous, for small inputs)
//   hashFile(path: string): Promise<string>                (worker thread)
#include <node_api.h>

#include "HashFileJob.hpp"
#include "NapiSupport.hpp"
#include "daisy/Sha256.hpp"
#include "daisy/Version.hpp"

namespace daisy::binding {

class DaisyNativeAddon {
 public:
  static napi_value init(napi_env env, napi_value exports) {
    const napi_property_descriptor methods[] = {
        {"version", nullptr, &DaisyNativeAddon::version, nullptr, nullptr, nullptr, napi_enumerable, nullptr},
        {"sha256", nullptr, &DaisyNativeAddon::sha256, nullptr, nullptr, nullptr, napi_enumerable, nullptr},
        {"hashFile", nullptr, &DaisyNativeAddon::hashFile, nullptr, nullptr, nullptr, napi_enumerable, nullptr},
    };
    Napi::check(env, napi_define_properties(env, exports, sizeof(methods) / sizeof(methods[0]), methods),
                "define exports");
    return exports;
  }

 private:
  static napi_value version(napi_env env, napi_callback_info /*info*/) {
    return NapiBoundary::guard(env, [&] { return Napi::string(env, Version::kString); });
  }

  static napi_value sha256(napi_env env, napi_callback_info info) {
    return NapiBoundary::guard(env, [&] {
      const CallbackArgs args(env, info);
      std::string holder;
      const auto bytes = Napi::toBytes(env, args.at(0, "data"), holder, "data");
      return Napi::string(env, Sha256::hexOf(bytes));
    });
  }

  static napi_value hashFile(napi_env env, napi_callback_info info) {
    return NapiBoundary::guard(env, [&] {
      const CallbackArgs args(env, info);
      return HashFileJob::start(env, Napi::toString(env, args.at(0, "path"), "path"));
    });
  }
};

}  // namespace daisy::binding

NAPI_MODULE_INIT() { return daisy::binding::DaisyNativeAddon::init(env, exports); }
