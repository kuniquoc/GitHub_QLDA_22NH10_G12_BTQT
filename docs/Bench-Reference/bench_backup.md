# bench backup

## Usage
`bench backup [OPTIONS]`

## Description
Backup sites specified. Executing the vanilla command will create a database dump, compress it, and save the data under the default backup location `./sites/{site}/private/backups`.

## Options
- `--backup-path`: Set path for saving all the files in this operation.
- `--backup-path-db`: Set path for saving database file.
- `--backup-path-conf`: Set path for saving config file.
- `--backup-path-files`: Set path for saving public file.
- `--backup-path-private-files`: Set path for saving private file.
- `--exclude`: Specify the DocTypes to not backup separated by commas.
- `--only`: Specify the DocTypes to backup separated by commas.

## Flags
- `--ignore-backup-conf`: Ignore excludes/includes set in config.
- `--with-files`: Take backup with private and public files.
- `--compress`: Compress private and public files.
- `--verbose`: Add verbosity.

## Examples
1. Backing up with the site's private and public files:
   ```
   bench --site {site} backup --with-files
   ```