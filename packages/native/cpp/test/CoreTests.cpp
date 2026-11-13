#include <filesystem>
#include <fstream>
#include <string>

#include "TestRunner.hpp"
#include "daisy/FileHasher.hpp"
#include "daisy/Sha256.hpp"

using daisy::FileHasher;
using daisy::Sha256;
using daisy::test::TestRunner;

namespace {

class CoreTests {
 public:
  static void registerAll(TestRunner& t) {
    // FIPS 180-4 / NIST test vectors.
    t.add("sha256 of empty input", [] {
      TestRunner::expectEqual(hex(""), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855");
    });
    t.add("sha256 of abc", [] {
      TestRunner::expectEqual(hex("abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
    });
    t.add("sha256 of the two-block message", [] {
      TestRunner::expectEqual(hex("abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"),
                              "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1");
    });
    t.add("sha256 of one million a in uneven chunks", [] {
      Sha256 h;
      const std::string chunk(997, 'a');
      std::size_t left = 1'000'000;
      while (left > 0) {
        const std::size_t n = std::min(left, chunk.size());
        h.update(std::string_view(chunk.data(), n));
        left -= n;
      }
      TestRunner::expectEqual(Sha256::toHex(h.finish()),
                              "cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0");
    });
    t.add("update after finish throws", [] {
      Sha256 h;
      h.finish();
      TestRunner::expectThrows([&] { h.update("x"); });
    });
    t.add("file hashing matches in-memory hashing across chunk sizes", [] {
      const auto path = std::filesystem::temp_directory_path() / "daisy-native-test.bin";
      std::string content;
      for (int i = 0; i < 200'003; ++i) content.push_back(static_cast<char>(i * 31 % 251));
      std::ofstream(path, std::ios::binary) << content;
      for (const std::size_t chunkSize : {1u, 63u, 64u, 65u, 4096u, 65536u}) {
        TestRunner::expectEqual(FileHasher(chunkSize).sha256Hex(path), hex(content));
      }
      std::filesystem::remove(path);
    });
    t.add("missing file throws", [] {
      TestRunner::expectThrows([] { (void)FileHasher().sha256Hex("/definitely/not/here.bin"); });
    });
  }

 private:
  static std::string hex(std::string_view text) {
    Sha256 h;
    h.update(text);
    return Sha256::toHex(h.finish());
  }
};

}  // namespace

int main() {
  TestRunner runner;
  CoreTests::registerAll(runner);
  return runner.run();
}
