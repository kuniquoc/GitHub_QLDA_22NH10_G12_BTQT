# Script API

Frappe provides a rich set of APIs for scripting. These APIs can be used in both Client Scripts and Server Scripts to interact with the system.

---

## Commonly Used APIs

### 1. `frappe.call`
Call a server-side method from the client:
```javascript
frappe.call({
    method: 'my_app.api.my_method',
    args: { key: 'value' },
    callback: function(response) {
        console.log(response.message);
    }
});
```

### 2. `frappe.get_doc`
Fetch a document:
```python
doc = frappe.get_doc('DocType', 'DocumentName')
```

### 3. `frappe.db.set_value`
Update a field in the database:
```python
frappe.db.set_value('DocType', 'DocumentName', 'fieldname', 'value')
```

---

Was this article helpful? Let us know your feedback!