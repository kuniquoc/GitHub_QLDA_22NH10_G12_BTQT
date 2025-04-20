# Site Configuration

## Introduction to Site Configuration

In Frappe, site configuration allows you to customize various aspects of your site's behavior, including database connections, email settings, system behavior, and more. These configurations are stored in JSON files and can be managed through the command line or programmatically.

Site-specific configurations provide a way to:

1. Define environment-specific settings (development, staging, production)
2. Configure technical parameters without changing code
3. Store sensitive information securely
4. Override default behavior of the framework

## Configuration Files

### Primary Configuration Files

Frappe uses two main configuration files:

1. **site_config.json**: Site-specific settings located in the site's directory
2. **common_site_config.json**: Shared settings for all sites, located in the `sites` directory

Here's an example of the file locations:

```
frappe-bench/
├── sites/
│   ├── common_site_config.json
│   └── mysite.example.com/
│       └── site_config.json
```

### Configuration Precedence

When Frappe looks for a configuration value, it follows this priority order:

1. Value in `site_config.json` (highest priority)
2. Value in `common_site_config.json`
3. Default value from the framework (lowest priority)

This allows you to override shared settings for specific sites as needed.

## Managing Site Configuration

### Using the Command Line

You can set configuration values using the `bench` command-line tool:

```bash
# Set a configuration option for a specific site
bench --site mysite.example.com set-config key value

# Set a boolean value
bench --site mysite.example.com set-config allow_cors true

# Set a JSON value
bench --site mysite.example.com set-config cors_headers '["Content-Type", "Authorization"]'

# Set a configuration option for all sites
bench config key value
```

To view current configuration:

```bash
# View a site's configuration
bench --site mysite.example.com get-site-config

# View a specific configuration value
bench --site mysite.example.com get-config key
```

### Using Python Code

You can also manage site configuration programmatically:

```python
# Get a configuration value
value = frappe.conf.get("key")

# Check if a configuration exists
if "smtp_server" in frappe.conf:
    # Use the SMTP server
    pass
```

## Common Configuration Options

### Database Settings

```json
{
  "db_name": "mysite",
  "db_password": "password",
  "db_host": "localhost",
  "db_port": 3306,
  "db_ssl_ca": "/path/to/ca.pem",
  "db_ssl_cert": "/path/to/cert.pem",
  "db_ssl_key": "/path/to/key.pem"
}
```

### Redis Settings

```json
{
  "redis_cache": "redis://localhost:13000",
  "redis_queue": "redis://localhost:11000",
  "redis_socketio": "redis://localhost:12000"
}
```

### Email Settings

```json
{
  "mail_server": "smtp.example.com",
  "mail_port": 587,
  "use_ssl": 1,
  "mail_login": "user@example.com",
  "mail_password": "password",
  "auto_email_id": "notifications@example.com",
  "email_sender_name": "Notifications",
  "always_use_account_email_id_as_sender": 0,
  "always_use_account_name_as_sender_name": 0
}
```

### System Settings

```json
{
  "developer_mode": 1,
  "disable_website_cache": 1,
  "logging": 1,
  "maintenance_mode": 0,
  "pause_scheduler": 0,
  "enable_telemetry": 0
}
```

### File Storage Settings

```json
{
  "max_file_size": 10485760,  // 10MB
  "max_attachment_size": 104857600  // 100MB
}
```

### Security Settings

```json
{
  "session_expiry": "06:00:00",  // 6 hours
  "cors_enabled": 1,
  "cors_origins": ["https://example.com"],
  "cors_headers": ["Content-Type", "Authorization"]
}
```

## Environment-Specific Configuration

You can create different configurations for different environments:

### Development Environment

```json
{
  "developer_mode": 1,
  "disable_website_cache": 1,
  "logging": 1,
  "db_host": "localhost"
}
```

### Production Environment

```json
{
  "developer_mode": 0,
  "disable_website_cache": 0,
  "logging": 0,
  "db_host": "production-db.example.com",
  "maintenance_mode": 0,
  "redis_cache": "redis://production-redis:6379/0"
}
```

## Security Best Practices

1. **Don't commit sensitive information**: Keep sensitive data like passwords out of version control
2. **Use environment variables** when possible:

```json
{
  "db_password": "{% raw %}{{ environ.DB_PASSWORD }}{% endraw %}"
}
```

3. **Restrict file permissions**: Ensure site_config.json has restricted permissions
4. **Use encrypted values** for highly sensitive data:

```bash
bench --site mysite.example.com set-encrypted-config secret_key "very-secret-value"
```

## Available Configuration Options

Here's a list of commonly used configuration options:

### Database Configuration

| Key | Description |
| --- | --- |
| `db_name` | Database name |
| `db_password` | Database password |
| `db_host` | Database host |
| `db_port` | Database port |
| `db_type` | Database type (default: MariaDB) |

### Redis Configuration

| Key | Description |
| --- | --- |
| `redis_cache` | Redis cache URL |
| `redis_queue` | Redis queue URL |
| `redis_socketio` | Redis socketio URL |

### Email Configuration

| Key | Description |
| --- | --- |
| `mail_server` | SMTP server |
| `mail_port` | SMTP port |
| `use_ssl` | Use SSL for email |
| `mail_login` | SMTP login |
| `mail_password` | SMTP password |

### System Configuration

| Key | Description |
| --- | --- |
| `developer_mode` | Enable developer mode |
| `disable_website_cache` | Disable website caching |
| `logging` | Enable logging |
| `maintenance_mode` | Enable maintenance mode |
| `pause_scheduler` | Pause background jobs |

### File Storage

| Key | Description |
| --- | --- |
| `max_file_size` | Maximum file upload size |
| `max_attachment_size` | Maximum email attachment size |
| `file_watcher_port` | Port for file watcher |

### Security Configuration

| Key | Description |
| --- | --- |
| `session_expiry` | Session expiry time |
| `cors_enabled` | Enable CORS |
| `cors_origins` | Allowed origins for CORS |
| `cors_headers` | Allowed headers for CORS |
| `allow_cors` | Legacy way to enable CORS |

## Troubleshooting Configuration Issues

### Common Issues

1. **Configuration not taking effect**
   - Make sure you've set the configuration for the correct site
   - Restart the Frappe server after changing configuration
   - Check the configuration precedence

2. **Error loading configuration**
   - Verify that your JSON syntax is valid
   - Check file permissions on the configuration files

3. **Cannot connect to database**
   - Verify database settings in site_config.json
   - Make sure the database server is running
   - Check network connectivity to the database server

### Debugging Configuration

To debug configuration issues:

```python
# In the Frappe console
import frappe
import json
print(json.dumps(frappe.conf, indent=2))
```

## Conclusion

Proper site configuration is essential for tailoring Frappe to your specific needs. By understanding how to manage configuration options, you can customize database connections, set email preferences, adjust system behavior, and implement environment-specific settings without modifying code. This flexibility is one of the key strengths of the Frappe Framework, allowing it to adapt to various deployment scenarios.