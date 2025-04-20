# bench transform-database

## Usage
`bench transform-database [OPTIONS] table`

## Description
The `transform-database` command allows you to manage the settings of your site's tables. At this point, you can switch engines and row_format settings for select tables on your site database.

## Options
- `--table`: Comma-separated name of tables to convert. To convert all tables, pass 'all'.
- `--engine`: Choice of storage engine for said table(s). Options available are `InnoDB` and `MyISAM`.
- `--row_format`: Set `ROW_FORMAT` parameter for said table(s). Options available are `DYNAMIC`, `COMPACT`, `REDUNDANT`, `COMPRESSED`.

## Examples
1. Change the engine of a table to `MyISAM`:
   ```
   bench --site {site} transform-database --table 'tabAccess Record' --engine 'MyISAM'
   ```
2. Convert all tables to the `DYNAMIC` row format:
   ```
   bench --site {site} transform-database --table 'all' --row_format 'DYNAMIC'
   ```