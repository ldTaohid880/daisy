/** Composition root of the main process (ADR 0011). Keep it to wiring. */
import { app } from 'electron';
import { Container } from '@daisy/di';
import { MainModule } from './MainModule.js';
import { MainTokens } from './tokens.js';

// No fallbacks (AGENTS.md 3c): a failure while wiring or starting ends the app with a non-zero exit code.
const container = new Container().load(new MainModule(!app.isPackaged));
container
  .resolve(MainTokens.Application)
  .start()
  .catch((error: unknown) => {
    console.error('Daisy failed to start:', error);
    app.exit(1);
  });
