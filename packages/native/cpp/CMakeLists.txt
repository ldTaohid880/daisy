cmake_minimum_required(VERSION 3.20)
project(daisy_native LANGUAGES CXX)

# Daisy native core and its Node-API addon (ADR 0013).
#   Addon via cmake-js:   pnpm --filter @daisy/native build       (packages/native/scripts/build-native.ts)
#   C++ tests only:       cmake -S packages/native/cpp -B build -DDAISY_BUILD_ADDON=OFF && ctest --test-dir build
#   Addon without cmake-js (Linux/macOS dev): -DNODE_INCLUDE_DIR=<node>/include/node

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

option(DAISY_BUILD_ADDON "Build the Node-API addon daisy_native.node" ON)
option(DAISY_BUILD_TESTS "Build the C++ unit tests" ON)

if(MSVC)
  add_compile_options(/W4 /permissive- /EHsc /utf-8)
else()
  add_compile_options(-Wall -Wextra -Wpedantic -Wconversion -Wno-sign-conversion)
endif()

# ── core: plain C++, no Node ──
add_library(daisy_core STATIC src/Sha256.cpp src/FileHasher.cpp)
target_include_directories(daisy_core PUBLIC include)

# ── tests ──
if(DAISY_BUILD_TESTS)
  enable_testing()
  add_executable(daisy_core_tests test/CoreTests.cpp)
  target_link_libraries(daisy_core_tests PRIVATE daisy_core)
  add_test(NAME daisy_core_tests COMMAND daisy_core_tests)
endif()

# ── addon ──
if(DAISY_BUILD_ADDON)
  if(CMAKE_JS_INC)
    set(DAISY_NODE_INCLUDE ${CMAKE_JS_INC})
  elseif(NODE_INCLUDE_DIR)
    set(DAISY_NODE_INCLUDE ${NODE_INCLUDE_DIR})
  else()
    message(FATAL_ERROR "Build the addon with cmake-js (pnpm --filter @daisy/native build) or pass -DNODE_INCLUDE_DIR=")
  endif()

  add_library(daisy_native SHARED
    binding/DaisyNativeAddon.cpp binding/NapiSupport.cpp binding/HashFileJob.cpp ${CMAKE_JS_SRC})
  set_target_properties(daisy_native PROPERTIES PREFIX "" SUFFIX ".node")
  target_include_directories(daisy_native PRIVATE ${DAISY_NODE_INCLUDE})
  target_compile_definitions(daisy_native PRIVATE NAPI_VERSION=9)
  target_link_libraries(daisy_native PRIVATE daisy_core ${CMAKE_JS_LIB})
  if(APPLE)
    target_link_options(daisy_native PRIVATE -undefined dynamic_lookup)
  endif()
  # Windows: generate node.lib from cmake-js's .def so the addon links against node.exe / electron.exe.
  if(MSVC AND CMAKE_JS_NODELIB_DEF AND CMAKE_JS_NODELIB_TARGET)
    execute_process(COMMAND ${CMAKE_AR} /def:${CMAKE_JS_NODELIB_DEF} /out:${CMAKE_JS_NODELIB_TARGET} ${CMAKE_STATIC_LINKER_FLAGS})
  endif()
endif()
