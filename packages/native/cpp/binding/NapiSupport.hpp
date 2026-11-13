#pragma once

// Small C++ helpers over Node-API (node_api.h). Node-API is ABI-stable, so one build works in every
// Electron version that supports NAPI_VERSION. Errors become C++ exceptions inside the binding and are
// turned into JavaScript errors at the boundary (NapiBoundary::guard).

#include <node_api.h>

#include <cstdint>
#include <functional>
#include <span>
#include <stdexcept>
#include <string>

namespace daisy::binding {

/** A JavaScript TypeError raised from C++. */
class NapiTypeError : public std::runtime_error {
 public:
  using std::runtime_error::runtime_error;
};

class Napi {
 public:
  static void check(napi_env env, napi_status status, const char* what);
  static napi_value string(napi_env env, const std::string& value);
  static std::string toString(napi_env env, napi_value value, const char* argName);
  /** Bytes of a Buffer, TypedArray or string argument. The span is valid during the call only. */
  static std::span<const std::uint8_t> toBytes(napi_env env, napi_value value, std::string& holder,
                                               const char* argName);
  static napi_valuetype typeOf(napi_env env, napi_value value);
};

/** Arguments of one call. */
class CallbackArgs {
 public:
  CallbackArgs(napi_env env, napi_callback_info info);
  [[nodiscard]] napi_value at(std::size_t index, const char* argName) const;

 private:
  napi_value argv_[4]{};
  std::size_t argc_ = 4;
};

/** Runs a binding body and converts C++ exceptions into thrown JavaScript errors. */
class NapiBoundary {
 public:
  static napi_value guard(napi_env env, const std::function<napi_value()>& body);
};

}  // namespace daisy::binding
