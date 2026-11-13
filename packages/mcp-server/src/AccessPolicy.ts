export type AccessLevel = 'read' | 'ask' | 'free';
export type Decision = 'allow' | 'ask' | 'refuse';

export interface ClientGrant {
  readonly clientId: string;
  readonly name: string;
  readonly access: AccessLevel;
  readonly reach: 'open-project' | 'recent-projects';
}

/**
 * Decides what happens to a request before anything is shown to the user (UI_DESIGN_PLAN.md D-59c).
 * Reads are always allowed; writes depend on the app's access level.
 */
export class AccessPolicy {
  decide(grant: ClientGrant, kind: 'read' | 'write'): Decision {
    if (kind === 'read') return 'allow';
    if (grant.access === 'read') return 'refuse';
    return grant.access === 'free' ? 'allow' : 'ask';
  }
}
