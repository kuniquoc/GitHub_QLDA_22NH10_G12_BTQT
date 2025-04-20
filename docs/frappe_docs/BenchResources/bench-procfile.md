# Bench Procfile

The `Procfile` in Bench defines the processes required to run a Frappe application in a development environment. It is used by `bench start` to manage these processes.

---

## Default Processes in the Procfile

1. **Watch**:
   Watches for changes in `.js` and `.css` files and rebuilds them.

2. **Schedule**:
   Runs the scheduler to enqueue background jobs.

3. **Worker**:
   Executes background jobs.

4. **SocketIO**:
   Manages real-time communication for Frappe.

5. **Web**:
   Starts the development server (Werkzeug).

---

## Example Procfile

```plaintext
watch: bench watch
schedule: bench schedule
worker: bench worker
socketio: /usr/bin/node apps/frappe/socketio.js
web: bench serve --port 8000
```

---

## Customizing the Procfile

You can modify the `Procfile` to add or remove processes as needed. For example, you can add a custom process for a specific app.

---

Was this article helpful? Let us know your feedback!