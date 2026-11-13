/** The JavaScript API of daisy_native.node (cpp/binding/DaisyNativeAddon.cpp). Keep both in step. */
export interface DaisyNativeAddon {
  version(): string;
  sha256(data: Uint8Array | string): string;
  hashFile(path: string): Promise<string>;
}

/** What the main process knows about the addon, for Help › About and diagnostics. */
export interface NativeStatus {
  readonly version: string;
  readonly path: string;
}
