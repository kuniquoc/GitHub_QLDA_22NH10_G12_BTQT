# Create a Site

## Introduction

In Frappe Framework, a site is a specific instance of your application with its own database. Each site comes with a database and may be customized through site-specific scripting, or apps may be installed on them. This tutorial will walk you through the process of creating a new site in your Frappe environment.

## Prerequisites

Before creating a site, make sure you:
- Have Bench installed and set up
- Have initialized a Frappe bench directory
- Have at least one app (like the `frappe` app) installed

## Create a new site

To create a new site, run the following command from your `frappe-bench` directory:

```bash
$ bench new-site library.localhost
```

This command will:
1. Create a new database for your site
2. Ask for your MariaDB/MySQL root password
3. Install the `frappe` app (which comes by default)
4. Prompt you to set the Administrator password for your site

You should see output similar to this:

```
MySQL root password:

Installing frappe...
Updating DocTypes for frappe        : [========================================] 100%
Set Administrator password:
*** Scheduler is disabled ***
Current Site set to library.localhost
```

Make sure to set a password for the Administrator user that you won't forget, as you'll need it to log in later.

## Site Directory Structure

After creating the site, you'll have a new folder named `library.localhost` in the `sites` directory with the following structure:

```
sites/library.localhost
├── indexes
│   └── web_routes
├── locks
├── logs
├── private
│   ├── backups
│   └── files
├── public
│   └── files
└── site_config.json
```

Notable directories and files:
- `private`: Contains database backups and private files that require authentication to access
- `public`: Contains files accessible without authentication, like website images
- `site_config.json`: Contains site-specific configuration, including database details

The `site_config.json` file will look something like this:

```json
{
  "db_name": "_ad03fa1a016ca1c4",
  "db_password": "pz1d2gN5y35ydRO5",
  "db_type": "mariadb"
}
```

## Access the site in your browser

Bench allows you to create multiple sites and access them separately in the browser on the same port. Frappe identifies which site to serve by matching the hostname of the request with the site name.

To access your site, go to:
```
http://library.localhost:8000
```

If this doesn't work, you may need to add an entry to your hosts file to map `library.localhost` to `localhost`. Bench has a convenient command to do just that:

```bash
$ bench --site library.localhost add-to-hosts
```

This will ask for your system password and add an entry to your `/etc/hosts` file.

## Install an app on the site

If you've created an app (like `library_management` from previous tutorials), you can install it on your site using:

```bash
$ bench --site library.localhost install-app library_management
```

To verify installed apps, run:

```bash
$ bench --site library.localhost list-apps
```

You should see `frappe` and any other apps you've installed, like `library_management`.

## Login to Desk

To access the Desk interface and start creating DocTypes:

1. Go to http://library.localhost:8000
2. Enter "Administrator" as the user and the password you set during site creation
3. Complete the setup wizard that appears after your first login

After completing the setup wizard, you'll see the Desk interface.

## Useful site commands

Here are some useful commands you can run for your site:

### Python Console
```bash
$ bench --site library.localhost console
```

### Database Backup
```bash
$ bench --site library.localhost backup
```

### See all site commands
```bash
$ bench --help
```

## Next Steps

Now that you have created a site and can access it, the next step is to start building your application by [creating DocTypes](https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype), which are the building blocks of your Frappe application.