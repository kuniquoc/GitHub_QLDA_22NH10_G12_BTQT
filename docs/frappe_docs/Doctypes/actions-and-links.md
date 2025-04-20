# Actions and Links in Frappe Framework

Actions and Links are ways to add custom operations and navigation options to DocTypes in Frappe. They appear as buttons and links in the form view, allowing users to perform operations or navigate to related documents.

## Document Actions

Document Actions appear as buttons in the form view, usually in the menu or toolbar. They trigger server-side Python methods or client-side JavaScript functions.

### Creating Document Actions

Document Actions can be added in two ways:

#### 1. Via DocType JSON

```json
{
  "actions": [
    {
      "label": "Create Invoice",
      "action": "create_invoice",
      "group": "Create"
    },
    {
      "label": "Send Email",
      "action": "send_email"
    }
  ]
}
```

#### 2. Via Python Hooks

You can also add actions dynamically in the controller's `get_actions` method:

```python
def get_actions(self):
    actions = []
    if self.status == "Draft":
        actions.append({
            "label": "Submit",
            "action": "submit_document",
            "group": "Status"
        })
    return actions
```

### Implementing Action Handlers

#### Server-Side Actions

For server-side actions, implement a method in the DocType controller:

```python
@frappe.whitelist()
def create_invoice(self):
    # Logic to create an invoice
    invoice = frappe.new_doc("Sales Invoice")
    invoice.customer = self.customer
    # Set more fields
    invoice.insert()
    frappe.msgprint(f"Invoice {invoice.name} created successfully")
    return invoice.name
```

#### Client-Side Actions

For client-side actions, implement a handler in the form script:

```javascript
frappe.ui.form.on('Customer', {
    send_email: function(frm) {
        frappe.call({
            method: 'frappe.email.queue.add',
            args: {
                'recipients': [frm.doc.email],
                'subject': 'Hello from Frappe',
                'message': 'This is a test email'
            },
            callback: function(r) {
                frappe.msgprint('Email sent successfully');
            }
        });
    }
});
```

## Document Links

Document Links appear in the "Links" section of the sidebar in the form view. They provide quick navigation to related documents.

### Creating Document Links

Links can be added in two ways:

#### 1. Via DocType JSON

```json
{
  "links": [
    {
      "link_doctype": "Sales Invoice",
      "link_fieldname": "customer",
      "group": "Invoices"
    },
    {
      "link_doctype": "Sales Order",
      "link_fieldname": "customer",
      "group": "Orders"
    }
  ]
}
```

#### 2. Via Python Hooks

You can also add links dynamically in the controller's `get_links` method:

```python
def get_links(self):
    links = []
    if self.has_membership:
        links.append({
            "link_doctype": "Membership",
            "link_fieldname": "customer",
            "group": "Memberships"
        })
    return links
```

## Custom Button Actions

In addition to document actions, you can add custom buttons in specific form views using client-side scripts:

```javascript
frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        if (frm.doc.status === 'Draft') {
            frm.add_custom_button(__('Create Invoice'), function() {
                frappe.model.open_mapped_doc({
                    method: "erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice",
                    frm: frm
                });
            }, __('Create'));
            
            frm.add_custom_button(__('Schedule Delivery'), function() {
                // Custom logic
            }, __('Create'));
        }
    }
});
```

## Best Practices

1. Group related actions together for better organization
2. Use clear and concise labels for actions and links
3. Implement proper validation before performing actions
4. Show confirmation dialogs for destructive actions
5. Show success/error messages after actions complete
6. Ensure proper permissions are checked before allowing actions
7. Consider the mobile experience when adding multiple actions