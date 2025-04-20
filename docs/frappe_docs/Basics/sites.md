# Frappe Sites

## Introduction to Sites

In Frappe, a "site" represents an instance of your application with its own database. Sites implement a multi-tenant architecture, allowing you to run multiple sites (tenants) from a single Frappe installation. Each site is isolated from others, with its own:

- Database
- Configuration
- Files and attachments
- Users and permissions

This architecture enables you to:
- Host multiple organizations or businesses
- Maintain development, testing, and production environments
- Create demo instances without affecting production data
- Scale horizontally by distributing sites across servers

## Site Directory Structure

Within the Frappe bench, sites are organized in the `sites` directory. Each site has its own folder structure:

```
sites/
├── assets/                # Shared static assets
├── common_site_config.json # Configuration shared by all sites
└── mysite.example.com/    # A specific site directory
    ├── locks/             # Lock files
    ├── private/           # Private files
    │   ├── backups/       # Database backups
    │   └── files/         # Private file attachments
    ├── public/            # Public files
    │   └── files/         # Public file attachments
    ├── site_config.json   # Site-specific configuration
    └── task-logs/         # Logs for background tasks
```

## Creating a New Site

To create a new site, you use the `bench new-site` command:

```bash
bench new-site mysite.example.com
```

This command will:
1. Create a database for the site
2. Set up the directory structure
3. Install the default Frappe applications
4. Create an administrator user

You can also specify additional parameters:

```bash
bench new-site mysite.example.com --db-name mysite_db --admin-password admin123 --install-app erpnext
```

## Site Configuration

Each site has its own configuration file called `site_config.json`, which contains site-specific settings:

```json
{
  "db_name": "mysite_db",
  "db_password": "database_password",
  "developer_mode": 1,
  "maintenance_mode": 0,
  "pause_scheduler": 0
}
```

Common configuration shared across all sites is stored in `common_site_config.json`:

```json
{
  "db_host": "localhost",
  "redis_cache": "redis://localhost:11000",
  "redis_queue": "redis://localhost:11001",
  "redis_socketio": "redis://localhost:11002"
}
```

## Managing Sites

### Listing Sites

To list all available sites:

```bash
bench site
```

### Setting the Current Site

To set a default site for commands:

```bash
bench use mysite.example.com
```

### Installing Apps on a Site

To install an app on a specific site:

```bash
bench --site mysite.example.com install-app erpnext
```

### Database Operations

To backup the database:

```bash
bench --site mysite.example.com backup
```

To restore from a backup:

```bash
bench --site mysite.example.com restore path/to/backup.sql.gz
```

### Migrating Schema Changes

When you update apps with schema changes:

```bash
bench --site mysite.example.com migrate
```

### Console Access

To access the Python console for a site:

```bash
bench --site mysite.example.com console
```

To run a Python script:

```bash
bench --site mysite.example.com execute myscript.py
```

### Site Maintenance

To enable maintenance mode (makes the site inaccessible to regular users):

```bash
bench --site mysite.example.com set-maintenance-mode on
```

## Multi-tenancy Features

### User Isolation

Users from one site cannot access another site's data. Each site has its own user authentication system.

### Data Separation

Each site has its own database, ensuring complete data isolation between sites.

### Custom Domains

You can configure multiple sites to run on different domains:

```bash
bench setup add-domain custom-domain.com --site mysite.example.com
```

## Site Management Best Practices

1. **Use descriptive site names**: Name sites based on their purpose or client name
2. **Regular backups**: Schedule automated backups for production sites
3. **Staging environment**: Maintain a separate site for testing before deploying to production
4. **Site configuration**: Keep sensitive settings in site_config.json, not in code
5. **Version control**: Track your site's configuration changes
6. **Resource planning**: Consider database size limits and allocate resources accordingly

## Common Site Issues and Solutions

### Site Not Accessible

If a site is not accessible, check:
- The site's maintenance mode setting
- DNS configuration
- Nginx/Apache setup
- Firewall rules

### Database Errors

For database connection issues:
- Verify database credentials in site_config.json
- Check if the database server is running
- Ensure the database exists and is properly initialized

### File Permission Issues

For file permission errors:
- Check the ownership of site directories
- Verify that the web server has appropriate permissions
- Use `bench setup permissions` to fix common permission issues

## Conclusion

Sites are a powerful feature of Frappe that enable multi-tenancy and flexible deployment options. Understanding how to create and manage sites is essential for effectively working with Frappe applications in development, testing, and production environments.