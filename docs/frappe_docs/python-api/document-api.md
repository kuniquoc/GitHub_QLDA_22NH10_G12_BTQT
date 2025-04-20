# Document API

A Document is an instance of a DocType. It is derived from the `frappe.model.Document` class and represents a single record in the database table.

## `frappe.get_doc`

### Usage
`frappe.get_doc(doctype, name)`  
Returns a Document object of the record identified by `doctype` and `name`. If no document is found, a `DoesNotExistError` is raised. If `doctype` is a Single DocType, `name` is not required.

#### Examples
```python
# Get an existing document
doc = frappe.get_doc('Task', 'TASK00002')
doc.title = 'Test'
doc.save()

# Get a single doctype
doc = frappe.get_doc('System Settings')
print(doc.timezone)  # Output: Asia/Kolkata
```

### Create a New Document
`frappe.get_doc(dict)`  
Returns a new Document object in memory which does not exist yet in the database.

#### Example
```python
# Create a new document
doc = frappe.get_doc({
    'doctype': 'Task',
    'title': 'New Task'
})
doc.insert()
```

## `frappe.new_doc`

An alternative way to create a new Document.

#### Example
```python
# Create a new document
doc = frappe.new_doc('Task')
doc.title = 'New Task 2'
doc.insert()
```

## `frappe.delete_doc`

Deletes the record and its children from the database.

#### Example
```python
frappe.delete_doc('Task', 'TASK00002')
```

## `frappe.get_last_doc`

Returns the last Document object created under the mentioned `doctype`.

#### Example
```python
# Get the last Task created
task = frappe.get_last_doc('Task')

# Get the last available Cancelled Task
task = frappe.get_last_doc('Task', filters={"status": "Cancelled"})
```

## `frappe.get_cached_doc`

Similar to `frappe.get_doc` but will look up the document in cache first before hitting the database.

#### Example
```python
doc = frappe.get_cached_doc('Task', 'TASK00002')
```

## Document Methods

### `doc.insert`
Inserts a new document into the database table. It will check for user permissions and execute `before_insert`, `validate`, `on_update`, `after_insert` methods if they are written in the controller.

#### Example
```python
doc.insert(
    ignore_permissions=True,  # Ignore write permissions during insert
    ignore_links=True,        # Ignore Link validation in the document
    ignore_if_duplicate=True, # Don't insert if DuplicateEntryError is thrown
    ignore_mandatory=True     # Insert even if mandatory fields are not set
)
```

### `doc.save`
Saves changes to an existing document. This will check for user permissions and execute `validate` before updating and `on_update` after updating values.

#### Example
```python
doc.save(
    ignore_permissions=True,  # Ignore write permissions during save
    ignore_version=True       # Do not create a version record
)
```

### `doc.delete`
Deletes the document record from the database table. This method is an alias to `frappe.delete_doc`.

#### Example
```python
doc.delete()
```

### `doc.reload`
Reloads the document from the database. This is useful when the document might have been updated by another process.

#### Example
```python
doc.reload()
```

### `doc.add_comment`
Adds a comment to this document. Will show up in the timeline in Form view.

#### Example
```python
# Add a simple comment
doc.add_comment('Comment', text='Test Comment')

# Add a comment of type Edit
doc.add_comment('Edit', 'Values changed')
```

### `doc.add_tag`
Adds a tag to a document. Tags are generally used to filter and group documents.

#### Example
```python
# Add tags
doc.add_tag('developer')
doc.add_tag('frontend')
```

### `doc.get_tags`
Returns a list of tags associated with the specific document.

#### Example
```python
# Get all tags
tags = doc.get_tags()
```

### `doc.notify_update`
Publishes a realtime event to indicate that the document has been modified. Client-side event handlers react to this event by updating the form.

#### Example
```python
doc.notify_update()
```

### `doc.db_set`
Sets a field value of the document directly in the database and updates the modified timestamp. This method does not trigger controller validations and should be used carefully.

#### Example
```python
# Update value in database and notify
doc.db_set('price', 2300, notify=True)
```

### `doc.append`
Appends a new item to a child table.

#### Example
```python
doc.append("childtable", {
    "child_table_field": "value",
    "child_table_int_field": 0,
})
```

### `doc.get_url`
Returns the Desk URL for this document.

#### Example
```python
url = doc.get_url()
print(url)  # Output: /app/task/TASK00002
```

### `doc.check_permission`
Throws an error if the current user has no permission for the provided `permtype`.

#### Example
```python
doc.check_permission(permtype='write')  # Throws if no write permission
```

### `doc.queue_action`
Runs a controller method in the background.

#### Example
```python
doc.queue_action('send_emails', emails=email_list, message='Howdy')
```

### `doc.get_children`
Returns a generator that yields an instance of `NestedSet` for each child record.

#### Example
```python
for child_doc in doc.get_children():
    print(child_doc.name)
```

This document provides a comprehensive overview of the Document API in Frappe Framework, including methods for creating, retrieving, updating, and deleting documents, as well as additional utilities for managing document metadata and relationships.