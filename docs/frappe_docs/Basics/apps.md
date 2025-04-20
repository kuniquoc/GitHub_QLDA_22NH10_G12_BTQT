# Frappe Apps

## Introduction to Frappe Apps

In Frappe, an "app" is a Python package that contains models, controllers, templates, and other assets that define the functionality of your application. Apps are modular components that can be installed on any Frappe site. This modular approach allows you to:

1. Develop independent components
2. Reuse functionality across different projects
3. Install or remove features without affecting other parts

## The App Structure

A Frappe app follows a standard Python package structure with some specific conventions:

```
my_custom_app/
├── LICENSE                # License file
├── MANIFEST.in            # Python package manifest
├── README.md              # Documentation
├── my_custom_app/         # Main Python package
│   ├── __init__.py        # Package initializer
│   ├── config/            # App configuration
│   ├── hooks.py           # Frappe hooks definition
│   ├── modules.txt        # List of modules
│   ├── my_custom_app/     # App module
│   │   └── ...            # Module contents
│   ├── patches.txt        # Database migration patches
│   ├── public/            # Public assets (JS, CSS, etc.)
│   ├── templates/         # HTML templates
│   └── www/               # Website pages
└── setup.py               # Python package setup
```

## Key Components of an App

### hooks.py

The `hooks.py` file is the central configuration file that tells Frappe how your app integrates with the framework:

```python
app_name = "my_custom_app"
app_title = "My Custom App"
app_publisher = "Your Company"
app_description = "Description of your app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@yourcompany.com"
app_license = "MIT"

# Includes in <head>
app_include_css = "/assets/my_custom_app/css/my_custom_app.css"
app_include_js = "/assets/my_custom_app/js/my_custom_app.js"

# Web Routes
website_route_rules = [
    {"from_route": "/blog", "to_route": "Blog Post"}
]

# Document Events
doc_events = {
    "User": {
        "after_insert": "my_custom_app.utils.user_creation"
    }
}
```

### modules.txt

This file lists the modules contained in your app:

```
My Custom App
```

### patches.txt

The `patches.txt` file contains a list of Python modules that should be executed when upgrading the app:

```
my_custom_app.patches.v1_0.update_field_values
my_custom_app.patches.v1_0.migrate_data
```

## Creating a New App

To create a new Frappe app, you use the `bench new-app` command:

```bash
bench new-app my_custom_app
```

This creates a new app with the basic structure mentioned above.

## App Installation and Management

### Installing an App

To install an app from GitHub:

```bash
bench get-app https://github.com/username/my_custom_app
```

To install it on a site:

```bash
bench --site mysite.local install-app my_custom_app
```

### Updating an App

To update an app:

```bash
bench update --apps my_custom_app
```

### Uninstalling an App

To uninstall an app from a site:

```bash
bench --site mysite.local uninstall-app my_custom_app
```

To remove an app completely from your bench:

```bash
bench remove-app my_custom_app
```

## App Dependencies

Apps can depend on other apps. Dependencies are specified in the `hooks.py` file:

```python
required_apps = ["frappe", "another_app"]
```

When you install an app, its dependencies are automatically installed first.

## Multiple Apps in a Project

A typical Frappe project consists of multiple apps working together:

1. **frappe** - The core framework
2. **your_domain_app** - Your main business logic
3. **additional_apps** - Extensions or integrations

This architecture allows you to:

- Separate concerns
- Develop features independently
- Reuse functionality
- Maintain a cleaner codebase

## App Development Best Practices

1. **Keep apps focused**: Each app should have a clear purpose
2. **Follow naming conventions**: Use lowercase with underscores
3. **Document your app**: Maintain a comprehensive README.md
4. **Version your app**: Use semantic versioning
5. **Use hooks appropriately**: Leverage Frappe's hooks system for integration
6. **Publish open source apps**: Share reusable components with the community

## App Configuration

Apps can be configured at various levels:

1. **Default configuration**: In the hooks.py file
2. **Site-specific configuration**: In the site_config.json file
3. **User-specific configuration**: Saved in the database

## Example: A Simple App

Here's what a simple Frappe app might contain:

1. **DocTypes**: Models defining your data structure
2. **Controllers**: Business logic in Python
3. **Web Pages**: Templates for web view
4. **Reports**: Data analysis views
5. **Scripts**: Client-side behavior
6. **API Methods**: Server endpoints for integration

## Conclusion

Frappe apps are the building blocks of your application. They provide a modular, maintainable way to develop complex business applications. By organizing your code into apps, you create reusable components that can be mixed and matched to build various solutions on the Frappe platform.