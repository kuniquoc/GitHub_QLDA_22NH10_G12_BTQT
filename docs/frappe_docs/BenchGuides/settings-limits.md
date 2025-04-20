# Setting Limits

You can configure limits for your Frappe site to optimize performance and resource usage.

---

## Common Settings

1. **Worker Processes**:
   Configure the number of worker processes in the `common_site_config.json` file:
   ```json
   "worker_processes": 4
   ```

2. **Request Timeout**:
   Set the request timeout in seconds:
   ```json
   "request_timeout": 300
   ```

3. **Max Connections**:
   Limit the maximum number of connections:
   ```json
   "max_connections": 100
   ```

---

Was this article helpful? Let us know your feedback!