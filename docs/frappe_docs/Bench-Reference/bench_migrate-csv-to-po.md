# bench migrate-csv-to-po

## Usage
`bench migrate-csv-to-po [OPTIONS]`

## Description
This command reads in your existing translations from CSV files, matches them with the existing POT file, and writes the result into `[app_module]/locale/[locale].po`. This is useful when switching from the old translation system to the new one.

## Options
- `--app`: Specify an app to migrate translations for. Default: all apps.
- `--locale`: Specify a locale to migrate translations for. Default: all locales.

## Examples
1. Migrate translations for a specific app and locale:
   ```
   bench migrate-csv-to-po --app erpnext --locale de
   ```