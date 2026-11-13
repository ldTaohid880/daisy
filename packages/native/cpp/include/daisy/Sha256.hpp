#pragma once

#include <array>
#include <cstddef>
#include <cstdint>
#include <span>
#include <string>
#include <string_view>

namespace daisy {

/**
 * Streaming SHA-256 (FIPS 180-4). Used for content-addressed assets (PLAN.md 10.4: AssetId is the
 * first 16 hex characters of the SHA-256 of the file).
 */
class Sha256 {
 public:
  using Digest = std::array<std::uint8_t, 32>;

  Sha256();

  void update(std::span<const std::uint8_t> data);
  void update(std::string_view text);
  /** Finishes the hash. The object must not be updated afterwards. */
  Digest finish();

  static std::string toHex(const Digest& digest);
  static std::string hexOf(std::span<const std::uint8_t> data);

 private:
  void processBlock(const std::uint8_t* block);

  std::array<std::uint32_t, 8> state_;
  std::array<std::uint8_t, 64> buffer_{};
  std::size_t bufferSize_ = 0;
  std::uint64_t totalBytes_ = 0;
  bool finished_ = false;
};

}  // namespace daisy
