# bench update-po-files

## Usage
`bench update-po-files [OPTIONS]`

## Description
This command syncs your existing translation files with the existing POT file, which holds all translatable strings. It removes outdated strings and adds new ones.

## Options
- `--app`: Specify an app to update the PO files for. Default: all apps.
- `--locale`: Specify a locale to update the PO file for. Default: all locales.

## Examples
1. Update PO files for a specific app and locale:
   ```
   bench update-po-files --app erpnext --locale de
   ```