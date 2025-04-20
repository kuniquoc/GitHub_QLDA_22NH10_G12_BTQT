# Virtual DocFields in Frappe Framework

Virtual DocFields are fields that do not exist in the database but are computed on the fly based on other fields. These fields are useful when you need to display information that is calculated from other fields in the DocType.

## Creating a Virtual Field

To create a Virtual Field, you need to set the `fieldtype` as `"Virtual"` when defining the field in the DocType JSON. Additionally, you need to implement a method in the controller class that computes the value of the field.

```json
{
  "fieldname": "full_name",
  "fieldtype": "Virtual",
  "label": "Full Name"
}
```

## Backend Implementation

In the DocType controller file, you need to define a method with the same name as the fieldname, prefixed with `get_`. This method will be called when the field value is accessed.

```python
def get_full_name(self):
    return f"{self.first_name} {self.last_name}"
```

## Frontend Implementation

For Client-side computation, you can set the virtual field value in Form Scripts:

```javascript
frappe.ui.form.on('User', {
    refresh: function(frm) {
        frm.set_value('full_name', frm.doc.first_name + ' ' + frm.doc.last_name);
    }
});
```

## Use Cases

Virtual DocFields are commonly used for:

1. Combining multiple fields (like first_name + last_name = full_name)
2. Displaying computed values (like age based on birth date)
3. Showing aggregate values from child tables (like total amount from line items)
4. Formatting or transforming data for display purposes

## Limitations

- Virtual fields cannot be used in filters or queries directly since they don't exist in the database
- Values are computed at runtime, which might have performance implications if calculation is complex
- Cannot be used for writing data, only for reading/displaying data