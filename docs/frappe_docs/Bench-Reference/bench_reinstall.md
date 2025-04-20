# bench reinstall

## Usage
`bench reinstall [OPTIONS]`

## Description
Reinstall a site with the current apps. This will wipe all site data and start afresh. This is considered a destructive operation, hence, contains an interactive confirmation prompt by default.

## Options
- `--admin-password`: Administrator Password for reinstalled site.
- `--mariadb-root-username`: Root username for MariaDB.
- `--mariadb-root-password`: Root password for MariaDB.

## Flags
- `--yes`: Skip confirmation for reinstall.

## Examples
1. Reinstall a site skipping the prompts for:
   - Confirmation for operation.
   - MariaDB Root Password.
   - Administrator Password.
   ```
   bench reinstall {site} --yes
   ```