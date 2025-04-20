# Frappe Apps

Frappe Apps are Python packages which use the Frappe platform. They can live anywhere on the Python path and must have an entry in the `apps.txt` file.

## Creating an App

Frappe ships with a boilerplate for a new app. The command `bench new-app app-name` helps you start a new app by starting an interactive shell.

Example:
```
bench new-app sample_app
```

This command creates an app with the following directory structure:
```
sample_app
├── license.txt
├── MANIFEST.in
├── README.md
├── sample_app
│   ├── __init__.py
│   ├── config
│   │   ├── desktop.py
│   │   └── __init__.py
│   ├── hooks.py
│   ├── modules.txt
│   ├── patches.txt
│   ├── templates
│   │   ├── generators
│   │   │   └── __init__.py
│   │   ├── pages
│   │   │   └── __init__.py
│   │   └── statics
│   └── setup.py
```

## Adding App to a Site

Once you have an app, whether it's the one you just created or any other you downloaded, you are required to do the following things:

1. Download the app via git:
```
bench get-app https://github.com/org/app_name
```

2. Install the app to your site:
```
bench --site site_name install-app app_name
```