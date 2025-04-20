# Configuring HTTPS

Configuring HTTPS ensures secure communication between your server and clients. Frappe supports HTTPS configuration using SSL certificates.

---

## Steps to Configure HTTPS

1. Obtain an SSL certificate from a trusted Certificate Authority (CA) or use Let's Encrypt for free SSL certificates.
2. Add the SSL certificate and key paths to your site's `site_config.json` file:
   ```json
   "ssl_certificate": "/path/to/certificate",
   "ssl_certificate_key": "/path/to/certificate-key"
   ```
3. Regenerate the Nginx configuration:
   ```bash
   bench setup nginx
   ```
4. Reload the Nginx service:
   ```bash
   sudo service nginx reload
   ```

---

Was this article helpful? Let us know your feedback!