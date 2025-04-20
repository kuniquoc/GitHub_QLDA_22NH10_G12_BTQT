# Setup Multitenancy

Multitenancy allows you to host multiple sites on a single Frappe instance.

---

## Steps to Enable Multitenancy

1. Enable DNS-based multitenancy:
   ```bash
   bench config dns_multitenant on
   ```

2. Add a new site:
   ```bash
   bench new-site [site-name]
   ```

3. Map the site to a domain:
   ```bash
   bench setup add-domain [domain-name]
   ```

4. Reload the Nginx service:
   ```bash
   sudo service nginx reload
   ```

---

Was this article helpful? Let us know your feedback!