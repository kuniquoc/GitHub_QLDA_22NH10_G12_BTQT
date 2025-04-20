# Create an App

## Introduction

A Frappe app is a Python package that contains models, controllers, web views, and other code related to a specific type of functionality. For example, if you're building a CRM system, you would create a CRM app. In this tutorial, we'll create a Library Management app.

## Create app

Before we start, make sure you're in a bench directory. To confirm, run `bench find .`:

```bash
$ bench find .
/home/frappe/frappe-bench is a bench directory!
```

To create our Library Management app, run the `new-app` command:

```bash
bench new-app library_management
```

You should get some prompts, and output like the following. You can enter information manually, or press enter to select the defaults:

```
App Title (default: Library Management): 
App Description: Library Management System
App Publisher: Faris Ansari
App Email: faris@example.com
App Icon (default 'octicon octicon-file-directory'): 
App Color (default 'grey'): 
App License (default 'MIT'): 
'library_management' created at /home/frappe/frappe-bench/apps/library_management

Installing library_management
$ ./env/bin/pip install -q -U -e ./apps/library_management
...
...
$ bench build --app library_management
yarn run v1.22.4
$ FRAPPE_ENV=production node rollup/build.js --app library_management
Production mode
✔ Built js/moment-bundle.min.js
✔ Built js/libs.min.js
✨  Done in 1.95s.
```

You will be prompted with details of your app, fill them up and an app named `library_management` will be created in the `apps` folder.

To see a complete list of all icons supported in the octicons library, check out [https://primer.style/octicons/](https://primer.style/octicons/)

## App directory structure

Your app directory structure should look something like this:

```
apps/library_management
├── README.md
├── library_management
│   ├── hooks.py
│   ├── library_management
│   │   └── __init__.py
│   ├── modules.txt
│   ├── patches.txt
│   ├── public
│   │   ├── css
│   │   └── js
│   ├── templates
│   │   ├── __init__.py
│   │   ├── includes
│   │   └── pages
│   │       └── __init__.py
│   └── www
└── pyproject.toml
```

- `library_management`: This directory will contain all the source code for your app
  - `public`: Store static files that will be served from Nginx in production
  - `templates`: Jinja templates used to render web views
  - `www`: Web pages that are served based on their directory path
  - `library_management`: Default Module bootstrapped with app
  - `modules.txt`: List of modules defined in the app
  - `patches.txt`: Patch entries for database migrations
  - `hooks.py`: Hooks used to extend or intercept standard functionality provided by the framework
  - `pyproject.toml`: Specifies how your app is built, you can optionally add 3rd party Python dependencies here which will get installed when your app is installed.

## Create a Site

Now that we've created our app, we need to create a site and install our app on it.

To create a site, run the following command:

```bash
bench new-site library.test
```

You will be prompted to create a new admin password and then a new user. After the site is created, you should see a message like:

```
Site library.test has been created
```

Now, let's install our app on our site:

```bash
bench --site library.test install-app library_management
```

After the app is installed, you should see a message like:

```
library_management has been installed
```

Finally, use the `bench start` command to start the development server:

```bash
bench start
```

Now, you can access your site at http://library.test:8000 if you've set up the development DNS. If not, you can access it at http://localhost:8000.

## Next Steps

In the next tutorial, we will [create our first DocType](https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype) for the Library Management app.