#include "NapiSupport.hpp"

namespace daisy::binding {

void Napi::check(napi_env env, napi_status status, const char* what) {
  if (status == napi_ok) return;
  const napi_extended_error_info* info = nullptr;
  napi_get_last_error_info(env, &info);
  const std::string detail = (info && info->error_message) ? info->error_message : "unknown Node-API error";
  throw std::runtime_error(std::string(what) + ": " + detail);
}

napi_value Napi::string(napi_env env, const std::string& value) {
  napi_value out = nullptr;
  check(env, napi_create_string_utf8(env, value.data(), value.size(), &out), "create string");
  return out;
}

napi_valuetype Napi::typeOf(napi_env env, napi_value value) {
  napi_valuetype type = napi_undefined;
  check(env, napi_typeof(env, value, &type), "typeof");
  return type;
}

std::string Napi::toString(napi_env env, napi_value value, const char* argName) {
  if (typeOf(env, value) != napi_string) throw NapiTypeError(std::string(argName) + " must be a string");
  std::size_t length = 0;
  check(env, napi_get_value_string_utf8(env, value, nullptr, 0, &length), "string length");
  std::string out(length, '\0');
  check(env, napi_get_value_string_utf8(env, value, out.data(), length + 1, &length), "read string");
  return out;
}

std::span<const std::uint8_t> Napi::toBytes(napi_env env, napi_value value, std::string& holder,
                                            const char* argName) {
  // Typed arrays first: Buffer is a Uint8Array, and on newer Node versions napi_is_buffer also accepts
  // other typed arrays, which must be rejected rather than read as raw bytes.
  bool isTypedArray = false;
  check(env, napi_is_typedarray(env, value, &isTypedArray), "is typed array");
  if (isTypedArray) {
    napi_typedarray_type type{};
    std::size_t length = 0;
    void* data = nullptr;
    napi_value arrayBuffer = nullptr;
    std::size_t offset = 0;
    check(env, napi_get_typedarray_info(env, value, &type, &length, &data, &arrayBuffer, &offset), "typed array info");
    if (type != napi_uint8_array && type != napi_uint8_clamped_array && type != napi_int8_array) {
      throw NapiTypeError(std::string(argName) + " must be a Uint8Array, Buffer or string");
    }
    return {static_cast<const std::uint8_t*>(data), length};
  }
  if (typeOf(env, value) == napi_string) {
    holder = toString(env, value, argName);
    return {reinterpret_cast<const std::uint8_t*>(holder.data()), holder.size()};
  }
  throw NapiTypeError(std::string(argName) + " must be a Uint8Array, Buffer or string");
}

CallbackArgs::CallbackArgs(napi_env env, napi_callback_info info) {
  Napi::check(env, napi_get_cb_info(env, info, &argc_, argv_, nullptr, nullptr), "read arguments");
}

napi_value CallbackArgs::at(std::size_t index, const char* argName) const {
  if (index >= argc_) throw NapiTypeError(std::string("Missing argument: ") + argName);
  return argv_[index];
}

napi_value NapiBoundary::guard(napi_env env, const std::function<napi_value()>& body) {
  try {
    return body();
  } catch (const NapiTypeError& error) {
    napi_throw_type_error(env, "ERR_DAISY_NATIVE_ARG", error.what());
  } catch (const std::exception& error) {
    napi_throw_error(env, "ERR_DAISY_NATIVE", error.what());
  }
  return nullptr;
}

}  // namespace daisy::binding
