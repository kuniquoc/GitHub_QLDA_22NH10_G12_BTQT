# Adding Custom Domains to Your Site

You can add multiple custom domains for your site by running the following command:

```bash
bench setup add-domain [desired-domain]
```

---

## Steps to Add a Custom Domain

1. Run the command:
   ```bash
   bench setup add-domain [desired-domain]
   ```
   You will be asked to specify the site for which you want to set the custom domain.

2. To set up SSL for your custom domain, use the following options:
   - `--ssl-certificate [path-to-certificate]`
   - `--ssl-certificate-key [path-to-certificate-key]`

### Example:
```bash
bench setup add-domain custom.erpnext.com --ssl-certificate /etc/letsencrypt/live/erpnext.cert --ssl-certificate-key /etc/letsencrypt/live/erpnext.key
```

---

## Domain Configuration

The domain configuration is stored in the respective site's `site_config.json` file:

```json
"domains": [
    {
        "ssl_certificate": "/etc/letsencrypt/live/erpnext.cert",
        "domain": "erpnext.com",
        "ssl_certificate_key": "/etc/letsencrypt/live/erpnext.key"
    }
]
```

---

## Applying Changes

1. Regenerate the Nginx configuration:
   ```bash
   bench setup nginx
   ```

2. Reload the Nginx service:
   ```bash
   sudo service nginx reload
   ```

This will put your custom domain into effect.

---

Was this article helpful? Let us know your feedback!