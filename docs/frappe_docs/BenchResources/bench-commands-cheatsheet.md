# Bench Commands Cheatsheet

Bench provides a variety of commands to manage your Frappe environment. Below is a quick reference for commonly used commands.

---

## Site Management

1. **Create a New Site**:
   ```bash
   bench new-site [site-name]
   ```

2. **Delete a Site**:
   ```bash
   bench drop-site [site-name]
   ```

3. **Backup a Site**:
   ```bash
   bench backup --site [site-name]
   ```

---

## App Management

1. **Install an App**:
   ```bash
   bench --site [site-name] install-app [app-name]
   ```

2. **Uninstall an App**:
   ```bash
   bench --site [site-name] uninstall-app [app-name]
   ```

---

## Development

1. **Start Development Server**:
   ```bash
   bench start
   ```

2. **Run Tests**:
   ```bash
   bench run-tests
   ```

---

## Production

1. **Setup Production Environment**:
   ```bash
   sudo bench setup production
   ```

2. **Restart Supervisor**:
   ```bash
   sudo service supervisor restart
   ```

---

Was this article helpful? Let us know your feedback!