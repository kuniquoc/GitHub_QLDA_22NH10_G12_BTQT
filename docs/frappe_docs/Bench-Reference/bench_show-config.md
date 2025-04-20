# bench show-config

## Usage
`bench show-config [OPTIONS]`

## Description
The applied configuration for your sites gets applied as a combination of the bench directory's `common_site_config.json` and the site's own `site_config.json`. Bench provides an interface to view the applied `frappe.conf` values for your sites.

## Flags
- `-f`, `--format`: Choose the format for listing apps installed on the specified site, options being "text" and "json". Default is "text".

## Examples
1. Show site config for all sites in JSON format:
   ```
   bench --site all show-config -f json
   ```
2. Show the site config in tabular form:
   ```
   bench --site {site} show-config --format text
   ```