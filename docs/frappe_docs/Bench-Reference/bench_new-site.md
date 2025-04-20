# bench new-site

## Usage
`bench new-site [OPTIONS] SITE`

## Description
Create a new Frappe site. This operation creates a new folder under `./sites` which will contain all the site information for the site and also creates a new database in your DBMS with all of Frappe's Modules and DocTypes installed.

## Options
- `--db-name`: Set the Database name for new site.
- `--db-user`: Set the Database user for new site.
- `--db-password`: Set the Database password for new site.
- `--db-type`: Select the Database Type for new site, options being "postgres" or "mariadb". Default is "mariadb".
- `--admin-password`: Specify the Administrator password for new site.

## Examples
1. Create a new site:
   ```
   bench new-site {site}
   ```
2. Create a new PostgreSQL site:
   ```
   bench new-site {site} --db-type postgres
   ```