# Diagnosing the Scheduler

The scheduler in Frappe is responsible for running background jobs. If the scheduler is not working as expected, you can diagnose and fix the issue.

---

## Common Commands for Diagnosis

1. **Check Scheduler Status**:
   ```bash
   bench doctor
   ```

2. **Enable the Scheduler**:
   ```bash
   bench --site [site-name] enable-scheduler
   ```

3. **Disable the Scheduler**:
   ```bash
   bench --site [site-name] disable-scheduler
   ```

4. **Trigger All Scheduled Jobs**:
   ```bash
   bench trigger-scheduler-event all
   ```

---

Was this article helpful? Let us know your feedback!