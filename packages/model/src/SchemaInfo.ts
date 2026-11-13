/** Schema version of stored projects (PLAN.md 12.7). Bump only with a migration and a fixture. */
export class SchemaInfo {
  static readonly current = 1;
}

export type NodeId = string;
export type PageId = string;
export type AssetId = string;
