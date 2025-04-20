# Sites

Frappe is a multitenant platform, and each tenant is called a site. Sites exist in a directory called `sites`, assumed as the current working directory when running a Frappe command or other services like Celery worker or a WSGI server.

## Sites Directory

The `sites` directory should contain the following:
- `apps.txt`: Contains a list of Python packages to treat as Frappe apps. Every Frappe app that you intend to use in your site should have an entry in this file.
- `common_site_config.json`: Configuration common to all sites can be put in this file.
- `assets`: Contains files required to be served for the browser client (e.g., `.js`, `.css`, `.png` files). This directory is auto-generated using the `bench build` command.
- `languages.txt`: Maps every language to its code.

## Adding a New Site

To add a new site, execute the following command in your Bench instance:
```
bench new-site SITENAME
```

## Setting a Site as the Current Site

To force a site to be used as the default site, execute the following:
```
bench use SITENAME
```

To verify, check the contents of `currentsite.txt` (found in the `sites` folder of your Bench instance). It should have `SITENAME`.