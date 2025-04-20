# DocType Controllers in Frappe Framework

Controllers are Python classes that extend the functionality of DocTypes. They contain methods that are triggered at different stages of a document's lifecycle and allow you to add custom business logic.

## Controller Structure

When you create a DocType, Frappe automatically generates two controller files:

1. **Python Controller**: `[module]/[doctype]/[doctype].py`
2. **JavaScript Controller**: `[module]/[doctype]/[doctype].js`

The Python controller extends the `Document` class from `frappe.model.document`.

## Standard Controller Methods

### Document Lifecycle Hooks

#### Before Events
These methods run before the corresponding database operations:

- `before_insert()`: Before a new document is inserted into the database
- `before_validate()`: Before validation runs
- `validate()`: During validation (most common hook point)
- `before_save()`: Before the document is saved
- `before_submit()`: Before a document is submitted
- `before_cancel()`: Before a document is cancelled
- `before_update_after_submit()`: Before changes to a submitted document are saved
- `before_delete()`: Before a document is deleted

#### After Events
These methods run after the corresponding database operations:

- `after_insert()`: After a new document is inserted
- `on_update()`: After a document is saved
- `on_submit()`: After a document is submitted
- `on_cancel()`: After a document is cancelled
- `on_update_after_submit()`: After changes to a submitted document are saved
- `on_trash()`: After a document is deleted (can still be restored at this point)
- `after_delete()`: After a document is deleted permanently

### Common Utility Methods

- `get_doc(doctype, name)`: Fetches a document from the database
- `get_list(doctype, filters, fields)`: Fetches a list of documents
- `get_value(doctype, name, fieldname)`: Fetches a specific field value
- `db.set_value(doctype, name, fieldname, value)`: Sets a field value directly in the database
- `throw(message)`: Raises an exception with a user-friendly message

## Example Controller

```python
import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
    # validate method is called before a document is saved
    def validate(self):
        # check if the member already has an active membership
        existing_membership = frappe.get_value(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,  # submitted
                "to_date": (">", frappe.utils.nowdate()),
            },
            "name",
        )
        
        if existing_membership:
            frappe.throw("Member already has an active membership")
            
        # check if the member has any outstanding fines
        unpaid_fines = frappe.get_list(
            "Library Fine",
            filters={
                "library_member": self.library_member,
                "paid": 0
            }
        )
        
        if len(unpaid_fines) > 0:
            frappe.throw("Member has unpaid fines. Please clear them first.")

    # on_submit is called when a document is submitted
    def on_submit(self):
        # create a new membership transaction
        frappe.get_doc({
            "doctype": "Library Transaction",
            "transaction_type": "Membership",
            "library_member": self.library_member,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "paid": self.paid
        }).insert(ignore_permissions=True)
```

## Best Practices

1. Put validation logic in the `validate` method
2. Use `before_save` for operations that must happen before the document is saved
3. Use `on_update` for operations that should happen after the document is saved
4. Always handle exceptions gracefully with user-friendly messages
5. Use `ignore_permissions=True` only when necessary and with proper validation
6. Keep controllers modular and follow the Single Responsibility Principle
7. Add docstrings to methods for better code documentation