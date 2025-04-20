# Server Script

A **Server Script** allows you to execute custom Python code on the server side. It is useful for automating backend processes, validations, and custom logic.

---

## Types of Server Scripts

1. **API**: Create custom API endpoints.
2. **Scheduler Event**: Run scripts on a schedule.
3. **Document Event**: Trigger scripts on document events like `Before Save`, `After Save`, etc.
4. **Permission Query**: Customize permissions dynamically.

---

## Example

### Custom API Endpoint
```python
# Create a custom API endpoint
@frappe.whitelist()
def custom_api():
    return {"message": "Hello, World!"}
```

---

Was this article helpful? Let us know your feedback!