# Background Services

Running an active Frappe environment requires the operation of various system-level services and some Frappe-specific processes. These services and processes ensure the smooth functioning of the system.

---

## System Processes

These processes are handled at the system level and may have configurations set up via Bench or other Frappe deployment management tools:

1. **MariaDB/PostgreSQL**: Database solutions for storing data.
2. **Redis**: Used for background worker queues and caching.
3. **NGINX**: Acts as a reverse proxy for production deployments.
4. **Supervisor**: Manages processes for non-containerized production deployments.

---

## Frappe Processes

These processes are defined in Frappe's codebase and are managed by Bench. They can be triggered manually or via a process manager:

1. **WSGI Server**:
   - Handles HTTP requests to Frappe.
   - In development, `bench serve` or `bench start` starts the Werkzeug server.
   - In production, Bench uses Gunicorn, which is automatically configured in Supervisor.

2. **Redis Worker Processes**:
   - Executes background jobs in the Frappe system.
   - Automatically started with `bench start` in development or configured in Supervisor for production.

3. **Scheduler Process**:
   - Schedules and enqueues background jobs.
   - Automatically started with `bench start` in development or configured in Supervisor for production.

---

## Configuration Files

- **Development**: Processes are defined in the `Procfile`.
- **Production**: Processes are defined in `config/supervisor.conf`.

---

Was this article helpful? Let us know your feedback!