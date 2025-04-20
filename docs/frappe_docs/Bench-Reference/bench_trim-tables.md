# bench trim-tables

## Usage
`bench trim-tables [OPTIONS]`

## Description
The `trim-tables` command modifies the schema of tables in your site's database to remove lingering columns that are no longer needed. This helps reduce backup sizes, optimize queries, and clean up redundant data.

## Options
- `-f`, `--format`: Set output format. Available options are JSON and TEXT. Defaults to TEXT.

## Flags
- `--dry-run`: Show what would be deleted.
- `--no-backup`: Do not backup the site. This is not recommended since this is a destructive operation.

## Examples
1. Check for ghost columns or old hidden fields:
   ```
   bench --site {site} trim-tables --dry-run
   ```