#include "daisy/FileHasher.hpp"

#include <fstream>
#include <stdexcept>
#include <vector>

#include "daisy/Sha256.hpp"

namespace daisy {

FileHasher::FileHasher(std::size_t chunkSize) : chunkSize_(chunkSize == 0 ? 1 : chunkSize) {}

std::string FileHasher::sha256Hex(const std::filesystem::path& path) const {
  std::ifstream in(path, std::ios::binary);
  if (!in) throw std::runtime_error("Cannot open file: " + path.string());
  Sha256 hasher;
  std::vector<std::uint8_t> chunk(chunkSize_);
  while (in) {
    in.read(reinterpret_cast<char*>(chunk.data()), static_cast<std::streamsize>(chunk.size()));
    const auto got = static_cast<std::size_t>(in.gcount());
    if (got > 0) hasher.update(std::span(chunk.data(), got));
  }
  if (in.bad()) throw std::runtime_error("Read failed: " + path.string());
  return Sha256::toHex(hasher.finish());
}

}  // namespace daisy
