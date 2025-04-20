# bench compile-po-to-mo

## Usage
`bench compile-po-to-mo [OPTIONS]`

## Description
The `compile-po-to-mo` command compiles PO files (human-readable translations) into MO files (binary translations) for use by the application. The binary files are stored in the `sites/assets/locale` folder of your bench.

## Options
- `--app`: Specify an app to compile PO files for. Default: all apps.
- `--locale`: Specify a locale to compile PO files for. Default: all locales.
- `--force`: Force re-compilation, even if the PO files didn't change.

## Examples
1. Compile PO files for a specific app and locale:
   ```
   bench compile-po-to-mo --app erpnext --locale de
   ```