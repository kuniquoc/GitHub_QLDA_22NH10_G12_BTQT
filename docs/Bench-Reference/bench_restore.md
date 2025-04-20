# bench restore

## Usage
`bench restore [OPTIONS] SQL_FILE_PATH`

## Description
Bench CLI can be used to restore an existing site to a previous state. Using the `bench restore` command, a site may be restored with the specific database and file restores. Downgrades aren't supported for Frappe Sites; when a downgrade is detected, an interactive prompt will pop up before the site restore begins.

## Options
- `--db-root-username`: Root username for MariaDB or Postgres.
- `--db-root-password`: Root password for MariaDB or Postgres.
- `--db-name`: Database name for site in case it is a new one.
- `--admin-password`: Administrator password for new site.
- `--install-app`: Install app after installation.
- `--with-public-files`: Restores the public files of the site, given path to its archive file.
- `--with-private-files`: Restores the private files of the site, given path to its archive file.

## Examples
1. Restore a site with files:
   ```
   bench --site {site} restore {path/to/database/file} --with-public-files {path/to/public/archive} --with-private-files {path/to/private/archive}
   ```
2. Reset the admin password for the restored site:
   ```
   bench --site {site} restore {path/to/database/file} --admin-password {admin-pass}
   ```