# Formatter For Link Fields

In cases where both a code and a name are maintained for an entity (e.g., for an Employee, there may be an Employee Code and Employee Name), and you want to show both the ID and name in a link field, you can create a formatter.

---

## Example

Here is an example of a formatter for the `Employee` DocType:

```javascript
frappe.form.link_formatters['Employee'] = function(value, doc) {
    if (doc.employee_name && doc.employee_name !== value) {
        return value + ': ' + doc.employee_name;
    } else {
        return value;
    }
};
```

---

## Notes

1. Both the primary key (`name`) and the descriptive name (e.g., `employee_name`) must be present in the document. The descriptive name field could be hidden.
2. This formatter needs to be loaded before the document is loaded and can be reused for all forms. You can also add it in `build.json`.

---

Was this article helpful? Let us know your feedback!