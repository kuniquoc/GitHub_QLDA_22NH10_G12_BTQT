# bench trim-database

## Usage
`bench trim-database [OPTIONS]`

## Description
The `trim-database` command drops any tables that seem to be remnants like ghost tables left by migrations or deletions. It will attempt a partial backup of the tables before dropping them.

## Options
- `-f`, `--format`: Set output format. Available options are JSON and Table. Defaults to Table.

## Flags
- `--dry-run`: Show what would be deleted.
- `--no-backup`: Do not backup the site prior to the trimming.

## Examples
1. Show what data will be deleted:
   ```
   bench --site {site} trim-database --dry-run
   ```
2. Get machine-parsable data in JSON format:
   ```
   bench --site {site} trim-database --format json
   ```