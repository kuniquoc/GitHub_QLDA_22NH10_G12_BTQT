# bench partial-restore

## Usage
`bench partial-restore [OPTIONS] SQL_FILE_PATH`

## Description
The `partial-restore` command may be used to restore sites using partial backups. The partial backup files may be gzip compressed or plain SQL files. In essence, you can restore anything from SQL files using this command.

## Flags
- `-v`, `--verbose`: Add verbosity.

## Examples
1. Restore with partial backups on a site:
   ```
   bench --site {site} partial-restore -v {/path/to/sql/file}
   ```