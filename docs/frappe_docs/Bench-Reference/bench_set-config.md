# bench set-config

## Usage
`bench set-config [OPTIONS] KEY VALUE`

## Description
Bench provides a wrapper command to insert or update values in the site config files. You can update values in your site's `site_config.json`, along with the bench directory's `common_site_config.json` through the same command.

## Flags
- `-g`, `--global`: Set value in the Bench's Common Site Config.
- `-p`, `--parse`: Parse given value instead of string. You can use this to set dict and list values.

## Examples
1. Enable tests for given site:
   ```
   bench --site {site} set-config allow_tests true
   ```
2. Set a dict value in your site's `frappe.conf`:
   ```
   bench --site {site} set-config backup '{"includes": ["Not", "ToDo"]}' --parse
   ```