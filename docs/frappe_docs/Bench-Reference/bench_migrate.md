# bench migrate

## Usage
`bench migrate [OPTIONS]`

## Description
The migrate command updates the site's state to the current available apps. It performs a range of tasks, in order:
- Run `before_migrate` Hooks.
- Run Application Patches.
- Synchronize Database Schema and Background Jobs.
- Synchronize Fixtures.
- Synchronize Dashboards, Desktop Icons, and Web Pages.
- Updates Translations.
- Run `after_migrate` Hooks.

## Flags
- `--skip-failing`: Skip patches that fail to run.
- `--skip-search-index`: Skip search indexing for web documents.

## Examples
1. Run migrations on an existing site:
   ```
   bench --site {site} migrate
   ```
2. Run migrations skipping rebuilding search index for web documents:
   ```
   bench --site {site} migrate --skip-search-index
   ```