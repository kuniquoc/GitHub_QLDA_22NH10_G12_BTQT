# Database API

The Frappe Framework provides a robust Database API to interact with the database. This API allows developers to perform CRUD operations, execute raw SQL queries, and manage database schema changes.

## `frappe.db.get_list`

### Usage
`frappe.db.get_list(doctype, filters=None, or_filters=None, fields=None, order_by=None, group_by=None, start=0, page_length=20, as_list=False, pluck=None)`

Returns a list of records from a DocType table. This is an ORM wrapper for a `SELECT` query. It applies user permissions for the session user. If the `fields` argument is not provided, it only returns the document names.

#### Examples
```python
# Get a list of Employee names
employees = frappe.db.get_list('Employee')

# Output
[{'name': 'HR-EMP-00008'},
 {'name': 'HR-EMP-00006'},
 {'name': 'HR-EMP-00010'},
 {'name': 'HR-EMP-00005'}]

# Pluck a specific field
employee_names = frappe.db.get_list('Employee', pluck='name')

# Output
['HR-EMP-00008', 'HR-EMP-00006', 'HR-EMP-00010', 'HR-EMP-00005']
```

## `frappe.db.exists`

### Usage
`frappe.db.exists(doctype, name_or_filters)`

Checks if a document exists in the database.

#### Examples
```python
# Check if a user exists by name
exists = frappe.db.exists("User", "jane@example.org")

# Check if a user exists by filters
exists = frappe.db.exists({"doctype": "User", "full_name": "Jane Doe"})
```

## `frappe.db.count`

### Usage
`frappe.db.count(doctype, filters=None)`

Returns the number of records for a given DocType and filters.

#### Examples
```python
# Count total Task records
total_tasks = frappe.db.count('Task')

# Count Open tasks
open_tasks = frappe.db.count('Task', {'status': 'Open'})
```

## `frappe.db.delete`

### Usage
`frappe.db.delete(doctype, filters=None)`

Deletes records from a DocType table that match the given filters.

#### Examples
```python
# Delete records from a custom table
frappe.db.delete("Route History", {
    "modified": ("<=", last_record_to_keep[0].modified),
    "user": user
})

# Delete all records from a table
frappe.db.delete("Error Log")
```

## `frappe.db.truncate`

### Usage
`frappe.db.truncate(doctype)`

Truncates a table in the database. This runs a `TRUNCATE TABLE` SQL command.

#### Examples
```python
# Truncate a table
frappe.db.truncate("Error Log")
```

## `frappe.db.sql`

### Usage
`frappe.db.sql(query, values=None, as_dict=False)`

Executes a raw SQL query. This is useful for complex queries that cannot be achieved using ORM methods.

#### Examples
```python
values = {'company': 'Frappe Technologies Inc'}
data = frappe.db.sql("""
    SELECT
        acc.account_number,
        gl.debit,
        gl.credit
    FROM `tabGL Entry` gl
    LEFT JOIN `tabAccount` acc
    ON gl.account = acc.name
    WHERE gl.company = %(company)s
""", values=values, as_dict=True)
```

## `frappe.db.set_value`

### Usage
`frappe.db.set_value(doctype, name, fieldname, value, update_modified=True)`

Sets a field's value in the database. This method does not call ORM triggers but updates the `modified` timestamp unless specified otherwise.

#### Examples
```python
# Update a single field
frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject')

# Update multiple fields
frappe.db.set_value('Task', 'TASK00002', {
    'subject': 'New Subject',
    'description': 'New Description'
})
```

## `frappe.db.get_value`

### Usage
`frappe.db.get_value(doctype, name_or_filters, fieldname, as_dict=False)`

Returns a document's field value or a list of values.

#### Examples
```python
# Get a single value
subject = frappe.db.get_value('Task', 'TASK00002', 'subject')

# Get multiple values
subject, description = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'])

# Get values as a dictionary
task_dict = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'], as_dict=True)
```

## `frappe.db.commit`

### Usage
`frappe.db.commit()`

Commits the current transaction. This is typically not required as Frappe automatically commits transactions at the end of a request.

#### Example
```python
frappe.db.commit()
```

## `frappe.db.rollback`

### Usage
`frappe.db.rollback()`

Rolls back the current transaction. This is useful for undoing changes in case of an error.

#### Example
```python
frappe.db.rollback()
```

## `frappe.db.add_index`

### Usage
`frappe.db.add_index(doctype, fields, index_name=None)`

Creates an index for a DocType on the specified fields.

#### Example
```python
frappe.db.add_index("Notes", ["id(10)", "content(500)"], index_name="notes_index")
```

## `frappe.db.add_unique`

### Usage
`frappe.db.add_unique(doctype, fields, constraint_name=None)`

Creates a unique constraint for a DocType on the specified fields.

#### Example
```python
frappe.db.add_unique("DoctypeName", ["field1", "field2"])
```

## Notes

- Use the Database API for safe and efficient database operations.
- Avoid using raw SQL queries unless absolutely necessary, as they bypass Frappe's ORM validations and permissions.