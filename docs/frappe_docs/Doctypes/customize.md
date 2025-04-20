# Customizing DocTypes in Frappe Framework

Frappe provides several ways to customize DocTypes without modifying their source code. This allows you to extend and adapt built-in DocTypes to your specific requirements without breaking compatibility with future updates.

## Customize Form

The "Customize Form" tool is the primary way to modify existing DocTypes without changing their source code. You can access it through:

1. System Menu > Customize Form, or
2. By clicking on the "Customize" button in any form

### What Can Be Customized

Using the Customize Form, you can:

- Add, remove, or modify fields
- Change field properties (label, required, read-only, etc.)
- Rearrange fields by changing their order
- Hide fields
- Set default values
- Change form layout (sections, columns, tabs)
- Modify naming settings
- Change form settings (allow email, allow print, etc.)
- Add custom scripts
- Add custom CSS

### Example: Customizing a Customer DocType

```javascript
// Custom Script for Customer
frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        frm.add_custom_button(__('Create Project'), function() {
            frappe.new_doc('Project', {
                customer: frm.doc.name
            });
        });
    },
    
    validate: function(frm) {
        if (frm.doc.credit_limit > 1000000 && !frm.doc.is_approved) {
            frappe.throw(__('Credit limit exceeds maximum allowed without approval'));
        }
    }
});
```

## Client Scripts

Client Scripts allow you to add custom JavaScript code to DocTypes. You can:

- Add custom validation logic
- Modify the user interface dynamically
- Add custom buttons and actions
- Change field values based on other fields
- Make API calls to the server
- Implement complex business rules

### How to Add a Client Script

1. Go to Customize Form > [DocType]
2. Scroll to the "Client Script" section
3. Add your JavaScript code
4. Click "Update"

## Server Scripts

Server Scripts allow you to add custom Python code to DocTypes without modifying their source files. This is useful for:

- Adding complex validation logic
- Implementing business rules
- Adding custom methods
- Interacting with other systems

### How to Add a Server Script

1. Go to "Server Script" list
2. Create a new Server Script
3. Select the DocType and event (before_insert, after_submit, etc.)
4. Add your Python code
5. Save and enable

### Example Server Script

```python
# Server Script for Sales Order
if "VIP" in doc.customer_group:
    # Apply special VIP discount
    for item in doc.items:
        item.discount_percentage = 10
    
    # Add a complimentary item for orders above a threshold
    if doc.grand_total > 10000:
        doc.append("items", {
            "item_code": "GIFT-ITEM-001",
            "qty": 1,
            "rate": 0
        })
```

## Custom Fields

You can add custom fields to DocTypes without modifying them:

1. Go to "Custom Field" list
2. Create a new Custom Field
3. Select the DocType and specify field properties
4. Save

### Example Custom Field

```json
{
  "dt": "Customer",
  "fieldname": "loyalty_points",
  "fieldtype": "Int",
  "label": "Loyalty Points",
  "insert_after": "customer_group"
}
```

## Property Setters

Property Setters allow you to modify existing field properties:

1. Go to "Property Setter" list
2. Create a new Property Setter
3. Select the DocType and field
4. Specify the property and new value
5. Save

### Example Property Setter

```json
{
  "doc_type": "Customer",
  "field_name": "credit_limit",
  "property": "reqd",
  "value": "1",
  "property_type": "Check"
}
```

## Best Practices for Customization

1. **Prefer customization over modification**: Always try to use customization tools before modifying source code
2. **Document your customizations**: Keep track of all customizations made for easier maintenance
3. **Test after upgrades**: Ensure your customizations still work after updating Frappe/ERPNext
4. **Use naming conventions**: For custom fields, use a prefix to identify your custom fields (e.g., "xyz_field_name")
5. **Limit client-side scripting**: Excessive client-side scripting can slow down the application
6. **Keep server scripts focused**: Each server script should have a single responsibility
7. **Consider performance impact**: Some customizations might affect system performance, especially with large datasets