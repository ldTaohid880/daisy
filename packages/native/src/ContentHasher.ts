/** SHA-256 of asset bytes and files (PLAN.md 10.4). Implemented by the C++ addon. */
export interface ContentHasher {
  hashBytes(data: Uint8Array | string): string;
  hashFile(path: string): Promise<string>;
}

/** AssetId = first 16 hex characters of the SHA-256 (PLAN.md 10.2). */
export class AssetIds {
  static fromHash(sha256Hex: string): string {
    return sha256Hex.slice(0, 16);
  }
}
