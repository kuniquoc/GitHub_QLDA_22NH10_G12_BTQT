# Let's Encrypt SSL Setup

Let's Encrypt provides free SSL certificates to secure your site. Frappe makes it easy to set up Let's Encrypt for your site.

---

## Steps to Set Up Let's Encrypt

1. Run the following command:
   ```bash
   bench setup lets-encrypt [site-name]
   ```

2. Follow the prompts to complete the setup.

3. Reload the Nginx service:
   ```bash
   sudo service nginx reload
   ```

---

Was this article helpful? Let us know your feedback!