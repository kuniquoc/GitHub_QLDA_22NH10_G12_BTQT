# Install and Setup Bench

## Introduction

Bench is the command line tool to manage Frappe apps and sites. This guide will walk you through the process of installing Bench and setting up a Frappe development environment.

## Installation

If you haven't installed Bench, follow the [Installation](https://docs.frappe.io/framework/user/en/installation) guide. After installation, you should be able to run commands that start with `bench`.

Run the following command to test your installation:

```bash
$ bench --version
5.1.0
```

## Create the frappe-bench directory

Let's create our project folder which will contain our apps and sites. Run the following command:

```bash
$ bench init frappe-bench
```

This will create a directory named `frappe-bench` in your current working directory. It will do the following:

1. Create a Python virtual environment under `env` directory.
2. Fetch and install the `frappe` app as a Python package.
3. Install node modules of `frappe`.
4. Build JS and CSS assets.

## Directory Structure

```
.
├── Procfile
├── apps
│   └── frappe
├── config
│   ├── pids
│   ├── redis_cache.conf
│   ├── redis_queue.conf
│   └── redis_socketio.conf
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   └── share
├── logs
│   ├── backup.log
│   └── bench.log
└── sites
    ├── apps.txt
    ├── assets
    └── common_site_config.json
```

- `env`: Python virtual environment
- `config`: Config files for Redis and Nginx
- `logs`: Log files for every process (web, worker)
- `sites`: Sites directory
  - `assets`: Static assets that served via Nginx in production
  - `apps.txt`: List of installed frappe apps
  - `common_site_config.json`: Site config that is available in all sites
- `apps`: Apps directory
  - `frappe`: The Frappe app directory
- `Procfile`: List of processes that run in development

## Start the Bench Server

Now that we have created our `frappe-bench` directory, we can start the Frappe web server by running the following command:

```bash
$ cd frappe-bench
$ bench start
```

This will start several processes including:
- A Python web server based on Gunicorn
- Redis servers for caching, job queuing and socketio pub-sub
- Background workers
- Node server for socketio
- A node server for compiling JS/CSS files

The web server will start listening on port `8000` but we don't have any sites yet to serve. Our next step is to create our app and create a site that will have this app installed.

> **Note:** Make sure not to close the terminal where `bench start` is running. To run bench commands, create another terminal and cd into the `frappe-bench` directory.

## Next Steps

Now that you have Bench installed and running, you can proceed to create apps and sites. The next step in the tutorial is to [Create an App](https://docs.frappe.io/framework/user/en/tutorial/create-an-app).