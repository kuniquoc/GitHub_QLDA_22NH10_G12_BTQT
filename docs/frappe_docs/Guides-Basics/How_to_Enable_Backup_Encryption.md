# How to Enable Backup Encryption

Files created during the backup process can be encrypted using an auto-generated key by checking the "Encrypt Backup" option. The data can be saved under the default or provided location.

## System Requirements

For macOS, ensure that `gnupg` is installed in the system. Use the following command to install `gnupg`:
```
brew install gnupg
```

Most Linux distributions already have GnuPG installed, and the current version will likely use GnuPG 2.0 by default.

## Steps to Enable Backup Encryption

1. Under the **Settings** tab, go to **System Settings**.
2. Inside the **Backups** section, check the **Encrypt Backup** checkbox.

### Backup Encryption Status

- Encrypted backups are stored at the same location as the general backups: `./sites/{site}/private/backups`.
- Encrypted backups can be downloaded from the `https://{site}/app/backups` page.
- Encrypted backups are differentiated using the key icon.

### Restoring Encrypted Backup Files

To restore encrypted backup files:
1. Use the following command to restore files without `--backup-encryption-key` as it is automatically picked from the Site Config:
```
bench restore SQL_FILE_PATH
```
2. In case of an unsuccessful restoration due to a wrong key, use `--backup-encryption-key` to provide the key to restore the files.

#### Usage:
- For full backup files:
```
bench --site {site} restore --backup-encryption-key {key} [OPTIONS]
```
- For partial backup files:
```
bench --site {site} partial-restore --backup-encryption-key {key} [OPTIONS]
```