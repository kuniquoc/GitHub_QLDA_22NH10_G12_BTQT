# bench generate-pot-file

## Usage
`bench generate-pot-file [OPTIONS]`

## Description
This command generates a template file for translations, holding all translatable strings of an app (but no translations). The template file will be written to the file `[app_module]/locale/main.pot`.

## Options
- `--app`: Specify an app to generate the POT file for. Default: all apps.

## Examples
1. Generate a POT file for a specific app:
   ```
   bench generate-pot-file --app erpnext
   ```