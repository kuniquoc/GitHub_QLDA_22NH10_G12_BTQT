# Executing Code On Doctype Events

To execute code when a DocType is inserted, validated (before saving), updated, submitted, cancelled, or deleted, you must write in the DocType's controller module.

## Controller Module

The controller module exists in the `doctype` folder in the module of the DocType. For example, the controller for `ToDo` exists in `frappe/desk/doctype/todo/todo.py`. A controller template is created when the DocType is created, which looks like this:

```python
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CustomType(Document):
    pass
```

## Adding Methods

In this module, you can add standard methods to the class that are called when a document of that type is created. Standard handlers include:

- `autoname`: Called while naming. You can set the `self.name` property in the method.
- `before_insert`: Called before a document is inserted.
- `validate`: Called before the document is saved. You can throw an exception if you don't want the document to be saved.
- `on_update`: Called after the document is inserted or updated in the database.
- `on_submit`: Called after submission.
- `on_cancel`: Called after cancellation.
- `on_trash`: Called after the document is deleted.