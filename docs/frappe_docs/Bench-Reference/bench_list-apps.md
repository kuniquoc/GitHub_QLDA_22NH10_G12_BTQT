# bench list-apps

## Usage
`bench list-apps [OPTIONS]`

## Description
List all the Frappe Applications installed on the specified site. The information shown by the command is fetched from the `Installed Applications` DocType which tracks the latest version of the apps the site was migrated to.

## Options
- `--format`, `-f`: Choose the format for listing apps installed on the specified site, options being "text" and "json". Default is "json".

## Examples
1. List apps installed on all sites:
   ```
   bench --site all list-apps
   ```
2. List apps installed on all sites in parsable JSON format:
   ```
   bench --site all list-apps --format json
   ```