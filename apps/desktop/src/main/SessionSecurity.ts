import { session } from 'electron';

/** Session-wide rules: every permission request is denied unless a feature adds an explicit rule. */
export class SessionSecurity {
  apply(): void {
    session.defaultSession.setPermissionRequestHandler((_webContents, _permission, callback) => {
      callback(false);
    });
  }
}
