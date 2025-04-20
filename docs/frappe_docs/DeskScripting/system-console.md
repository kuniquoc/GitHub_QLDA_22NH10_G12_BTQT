# System Console

The **System Console** in Frappe is a powerful tool that allows you to execute Python code directly on the server. It is useful for debugging, testing, and performing administrative tasks.

---

## How to Access the System Console

1. Ensure your role is **System Manager**.
2. Type "System Console" in the awesomebar and hit enter.

---

## Features

- Execute Python code directly on the server.
- Access Frappe's backend APIs and database.
- Perform administrative tasks like updating records, running scripts, and debugging.

---

## Example

### Update a Field for All Records
```python
for user in frappe.get_all('User', filters={'enabled': 1}):
    frappe.db.set_value('User', user.name, 'send_welcome_email', 1)
```

---

Was this article helpful? Let us know your feedback!