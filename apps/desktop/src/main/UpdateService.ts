import electronUpdater from 'electron-updater';

/**
 * Updates from GitHub Releases (electron-builder.yml › publish). Downloads in the background;
 * installing waits for quit (docs/engineering/RELEASING.md).
 */
export class UpdateService {
  start(): void {
    const { autoUpdater } = electronUpdater;
    autoUpdater.autoDownload = true;
    autoUpdater.autoInstallOnAppQuit = true;
    autoUpdater.on('error', (err) => {
      console.error('Update check failed', err);
    });
    void autoUpdater.checkForUpdatesAndNotify();
  }
}
