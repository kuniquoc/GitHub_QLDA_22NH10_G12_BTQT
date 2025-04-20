# Email Notifications For Failed Background Jobs

Frappe handles job failures in the following ways:

1. Logs the failure in `Scheduler Log` and `logs/worker.error.log`.
2. Keeps a lock file to prevent further execution if the lock file exists.
3. Raises `LockTimeoutError` if the lock file is older than 10 minutes.

## Configuring Email Notifications

To configure email notifications for scheduler errors, add the following to `sites/common_site_config.json`:

```json
{
  "celery_error_emails": {
    "ADMINS": [
      ["Person 1", "person1@example.com"],
      ["Person 2", "person2@example.com"]
    ],
    "SERVER_EMAIL": "exceptions@example.com"
  }
}
```

**Note**: The system uses the local mail server on port 25 to send emails.