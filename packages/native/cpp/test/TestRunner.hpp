#pragma once

#include <functional>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace daisy::test {

/** Minimal test runner: register cases, run them, return a process exit code for CTest. */
class TestRunner {
 public:
  void add(std::string name, std::function<void()> body) { cases_.emplace_back(std::move(name), std::move(body)); }

  int run() const {
    int failed = 0;
    for (const auto& [name, body] : cases_) {
      try {
        body();
        std::cout << "  ok    " << name << '\n';
      } catch (const std::exception& error) {
        ++failed;
        std::cout << "  FAIL  " << name << ": " << error.what() << '\n';
      }
    }
    std::cout << cases_.size() - failed << " passed, " << failed << " failed\n";
    return failed == 0 ? 0 : 1;
  }

  static void expectEqual(const std::string& actual, const std::string& expected) {
    if (actual != expected) throw std::runtime_error("expected " + expected + " but got " + actual);
  }

  template <typename Fn>
  static void expectThrows(Fn&& fn) {
    try {
      fn();
    } catch (const std::exception&) {
      return;
    }
    throw std::runtime_error("expected an exception");
  }

 private:
  std::vector<std::pair<std::string, std::function<void()>>> cases_;
};

}  // namespace daisy::test
