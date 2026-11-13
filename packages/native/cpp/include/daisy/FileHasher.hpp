#pragma once

#include <cstddef>
#include <filesystem>
#include <string>

namespace daisy {

/** Hashes a file from disk in fixed-size chunks, so large videos never load into memory at once. */
class FileHasher {
 public:
  explicit FileHasher(std::size_t chunkSize = 1 << 16);

  /** Lower-case hex SHA-256 of the file. Throws std::runtime_error with a readable message. */
  [[nodiscard]] std::string sha256Hex(const std::filesystem::path& path) const;

 private:
  std::size_t chunkSize_;
};

}  // namespace daisy
