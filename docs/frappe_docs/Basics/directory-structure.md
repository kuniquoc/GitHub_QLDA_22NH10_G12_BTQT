# Directory Structure

In this section, you will learn about the directory structure of Frappe applications and how different components are organized within the framework.

## Bench Directory Structure

When you set up a new Frappe environment using Bench, it creates a structured directory layout. Let's explore the main components of this structure:

```
frappe-bench/
│
├── apps/                      # Contains all Frappe apps
│   ├── frappe/               # Frappe framework app
│   └── my_custom_app/        # Your custom apps
│
├── config/                    # Configuration files
│   ├── redis_cache.conf      # Redis cache config
│   ├── redis_queue.conf      # Redis queue config
│   ├── redis_socketio.conf   # Redis socketio config
│   ├── supervisor.conf       # Supervisor config
│   └── nginx.conf            # Nginx config
│
├── env/                       # Python virtual environment
│
├── logs/                      # Log files
│   ├── bench.log             # Bench operations log
│   ├── frappe.log            # Frappe framework log
│   └── worker.log            # Background workers log
│
├── node_modules/              # Node.js modules
│
├── sites/                     # Multi-tenant sites
│   ├── assets/               # Static assets (JS, CSS, images)
│   ├── common_site_config.json # Shared site configuration
│   ├── currentsite.txt       # Current default site
│   └── site1.local/          # Individual site folder
│       ├── private/          # Site's private files
│       │   ├── backups/      # Database backups
│       │   └── files/        # Private file attachments
│       ├── public/           # Site's public files
│       │   └── files/        # Public file attachments
│       ├── site_config.json  # Site-specific configuration
│       └── task-logs/        # Logs for background tasks
│
└── Procfile                   # Process configuration for Honcho
```

## App Directory Structure

Each Frappe app follows a standard structure. Let's explore the structure of a typical app:

```
my_custom_app/
│
├── my_custom_app/            # Python package
│   │
│   ├── __init__.py           # Package initializer
│   │
│   ├── hooks.py              # App hooks and configuration
│   │
│   ├── patches.txt           # Database migration patches
│   │
│   ├── modules.txt           # List of modules in the app
│   │
│   ├── public/               # Static assets
│   │   ├── css/              # CSS files
│   │   ├── js/               # JavaScript files
│   │   └── images/           # Image files
│   │
│   ├── templates/            # Jinja templates
│   │   ├── includes/         # Reusable template parts
│   │   └── pages/            # Page templates
│   │
│   ├── config/               # Configuration files
│   │   ├── desktop.py        # Desktop icons configuration
│   │   └── docs.py           # Documentation configuration
│   │
│   └── module_name/          # A module in your app
│       ├── __init__.py       # Module initializer
│       │
│       ├── doctype/          # DocTypes (models)
│       │   └── my_doctype/   # A specific DocType
│       │       ├── __init__.py
│       │       ├── my_doctype.py      # DocType controller
│       │       ├── my_doctype.js      # Client-side script
│       │       └── my_doctype.json    # DocType schema
│       │
│       ├── page/             # Pages
│       │   └── my_page/      # A specific page
│       │       ├── my_page.js       # Client-side script
│       │       ├── my_page.py       # Server-side script
│       │       └── my_page.json     # Page configuration
│       │
│       ├── report/           # Reports
│       │   └── my_report/    # A specific report
│       │       ├── my_report.js       # Client-side script
│       │       ├── my_report.py       # Server-side script
│       │       └── my_report.json     # Report configuration
│       │
│       ├── web_form/         # Web Forms
│       │   └── my_web_form/  # A specific web form
│       │       ├── my_web_form.js     # Client-side script
│       │       ├── my_web_form.py     # Server-side script
│       │       └── my_web_form.json   # Web form configuration
│       │
│       └── print_format/     # Print Formats
│           └── my_print_format/ # A specific print format
│               └── my_print_format.json # Print format configuration
│
├── setup.py                  # Python package setup file
│
├── requirements.txt          # Python dependencies
│
├── license.txt               # License information
│
└── README.md                 # Project documentation
```

## Site Directory Structure

Each site in Frappe has its own directory within the `sites` folder. This is how a typical site directory is organized:

```
site1.local/
│
├── private/                  # Private files
│   ├── backups/              # Database backups
│   └── files/                # Private file attachments
│
├── public/                   # Public files
│   └── files/                # Public file attachments
│
├── site_config.json          # Site-specific configuration
│
└── task-logs/                # Logs for background tasks
```

## Understanding the Key Components

### Hooks.py

The `hooks.py` file is a central configuration file that defines how your app integrates with the Frappe framework. It contains various hooks like:

```python
app_name = "my_custom_app"
app_title = "My Custom App"
app_publisher = "Your Name"
app_description = "A custom app built on Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your@email.com"
app_license = "MIT"

# Hooks for including JS, CSS, Python files
app_include_js = ["/assets/my_custom_app/js/my_custom_app.js"]
app_include_css = ["/assets/my_custom_app/css/my_custom_app.css"]

# Auto-created doctypes to be included in the app
fixtures = ["Custom Field", "Custom Script"]

# DocType events hooks
doc_events = {
    "User": {
        "after_insert": "my_custom_app.events.user_creation"
    }
}

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "my_custom_app.tasks.daily"
    ],
}
```

### DocType Structure

A DocType is the fundamental data model in Frappe. Each DocType has:

1. **JSON Schema File**: Defines fields, permissions, and other metadata.
2. **Controller Class**: Contains business logic and event handlers.
3. **Client-side Script**: Contains form behavior and client-side validations.

### Modules and Organization

Modules help organize DocTypes and other components into logical groups. Each module can contain:

- DocTypes
- Pages
- Reports
- Web Forms
- Print Formats

## Best Practices

1. **Keep modules organized**: Group related DocTypes and components in the same module.
2. **Follow naming conventions**: Use lowercase with underscores for filenames and module names.
3. **Use patches.txt for migrations**: When making database schema changes, create migration patches.
4. **Utilize hooks.py effectively**: Configure app behavior through hooks rather than modifying framework files.
5. **Separate configuration from code**: Use site_config.json and customize modules for site-specific settings.

## Conclusion

Understanding the directory structure of Frappe applications is essential for effective development. Each component has its designated place, making it easier to locate and maintain code as your application grows.