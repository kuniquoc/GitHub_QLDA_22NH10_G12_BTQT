# Setup Production

Setting up a production environment ensures that your Frappe instance is optimized for performance and reliability.

---

## Steps to Set Up Production

1. Install the production setup:
   ```bash
   sudo bench setup production
   ```

2. Configure Supervisor and Nginx:
   ```bash
   bench setup supervisor
   bench setup nginx
   ```

3. Reload the services:
   ```bash
   sudo service supervisor restart
   sudo service nginx reload
   ```

---

Was this article helpful? Let us know your feedback!