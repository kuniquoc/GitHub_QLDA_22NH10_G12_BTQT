# Installation

> Note: For production deployments or docker based development use [frappe_docker](https://github.com/frappe/frappe_docker).

## System Requirements

This guide assumes you are using a personal computer, VPS or a bare-metal server. You also need to be on a *nix system, so any Linux Distribution and macOS is supported. If you're a Windows user, you could use Ubuntu in WSL. We officially support only the following distributions.

1. [macOS](#macos)
2. [Debian / Ubuntu](#debian--ubuntu)

Learn more about the architecture [here](https://docs.frappe.io/framework/basics/architecture).

## Pre-requisites

| Dependency                                  | Usage                                |
|--------------------------------------------|--------------------------------------|
| MariaDB 10.6.6+ (11.3 is recommended on develop) | Database                       |
| Python 3.10/11/12                           | Server Side Language                |
| Node 18 or 20                               | JS Runtime                          |
| Redis 6                                     | Caching and realtime updates        |
| yarn 1.12+                                  | JS dependency manager               |
| pip 20+                                     | Python dependency manager           |
| wkhtmltopdf (version 0.12.5 with patched qt)| PDF generation                      |
| cron                                        | Bench's scheduled jobs: automated certificate renewal, scheduled backups |

## Install Bench CLI

Install bench via pip

```bash
pip install frappe-bench
```

> Note: depending on your OS and version of python, you may need to use `pip3` instead of `pip`.

Pip discourages system-wide installations, thus you might have to do something equivalent to `source rcfile`. Will vary depending on your OS. E.g. for Ubuntu

```bash
source ~/.profile
```

You may need to manually add the directory its installed to into your PATH. The output of pip install should indicate this if required. You can run something like this with the correct path to achieve this.

```bash
echo "export PATH=/path/to/bin:$PATH" >> ~/.profile
source ~/.profile
```

Depending on your OS version and python/pip version, you may get an error here regarding an `externally-managed-environment`. You can work around this for now by running or use [virtualenv](https://virtualenv.pypa.io/en/latest/).

```bash
pip install frappe-bench --break-system-packages
```

An alternative method to do this is with [uv](https://github.com/astral-sh/uv) and a shell alias

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Add `alias bench='uvx --from frappe-bench bench'` to your shell rc file (.zshrc, .bashrc or similar)

Confirm the bench installation by checking the version

```bash
bench --version
```

Create your first bench.

```bash
cd ~
bench init <directory name>
```

Congratulations, you have installed bench onto your system.

## macOS

Install command line version of Xcode tools.

```bash
xcode-select --install
```

Install [Homebrew](https://brew.sh/). It makes it easy to install packages on macOS.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

(It may prompt you to run some additional commands at the end, which will ensure `brew` is available in your PATH)

Install wkhtmltopdf

```bash
curl -L https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-2/wkhtmltox-0.12.6-2.macos-cocoa.pkg -O

installer -pkg wkhtmltox-0.12.6-2.macos-cocoa.pkg -target ~
```

Now, you can easily install the required packages by running the following command

```bash
brew install python@3.12 git redis mariadb@10.6 node@18 postgresql pkg-config mariadb-connector-c
```

Now, edit the MariaDB configuration file (this step is not required for Frappe v15.21.0 or above).

```bash
nano /usr/local/etc/my.cnf
```

For Apple Silicon (non Intel macs), the path for the MariaDB config is

```bash
nano /opt/homebrew/etc/my.cnf
```

And add this configuration

```
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
bind-address = 127.0.0.1

[mysql]
default-character-set = utf8mb4
```

Now, just restart the mysql service and you are good to go.

```bash
brew services restart mariadb@10.6
```

### Install Yarn

Install yarn using npm

```bash
npm install -g yarn
```

## Debian / Ubuntu

You should be running Debian 12+ or Ubuntu 22.04+, otherwise you may have issues with some of the packages.

Update your system's package index

```bash
sudo apt update
```

Install `git`, `python`, and `redis`

```bash
sudo apt install git python-is-python3 python3-dev python3-pip redis-server libmariadb-dev mariadb-server mariadb-client pkg-config
```

During this installation you'll be prompted to set the MySQL root password. If you are not prompted, you'll have to initialize the MySQL server setup yourself. You can do that by running the command:

```bash
mariadb-secure-installation
```

> Remember: only run it if you're not prompted the password during setup.

It is really important that you remember this password, since it'll be useful later on.

Now, edit the MariaDB configuration file (this step is not required for Frappe v15.21.0 or above).

```bash
nano /etc/mysql/my.cnf
```

And add this configuration

```
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
```

Now, just restart the MariaDB service and you are good to go.

```bash
sudo systemctl restart mariadb
```

### Install Node

We recommend installing node using [nvm](https://github.com/nvm-sh/nvm)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

After nvm is installed, you may have to close your terminal and open another one. Now run the following command to install node.

```bash
nvm install 18
```

Verify the installed version, by running:

```bash
node -v
```

Finally, install `yarn` using `npm`

```bash
npm install -g yarn
```

### Install wkhtmltopdf

```bash
sudo apt install xvfb libfontconfig
```

Download and install wkhtmltopdf package from [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

```bash
sudo dpkg -i wkhtmltox_file.deb
```

## Additional Installation Notes

### Install Bench CLI - Alternative Method

Install bench via pip

```bash
pip install frappe-bench
```

> Note: depending on your OS and version of python, you may need to use `pip3` instead of `pip`.

Pip discourages system-wide installations, thus you might have to do something equivalent to `source rcfile`. Will vary depending on your OS. E.g. for Ubuntu

```bash
source ~/.profile
```

You may need to manually add the directory its installed to into your PATH. The output of pip install should indicate this if required. You can run something like this with the correct path to achieve this.

```bash
echo "export PATH=/path/to/bin:$PATH" >> ~/.profile
source ~/.profile
```

Depending on your OS version and python/pip version, you may get an error here regarding an `externally-managed-environment`

You can work around this for now by running or use [virtualenv](https://virtualenv.pypa.io/en/latest/)

```bash
pip install frappe-bench --break-system-packages
```

An alternative method to do this is with [uv](https://github.com/astral-sh/uv) and a shell alias

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Add `alias bench='uvx --from frappe-bench bench'` to your shell rc file (.zshrc, .bashrc or similar)

Confirm the bench installation by checking the version

```bash
bench --version
```

Create your first bench.

```bash
cd ~
bench init <directory name>
```

Congratulations, you have installed bench onto your system.