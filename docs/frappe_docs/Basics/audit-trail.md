# Audit Trail

## Introduction to Audit Trail in Frappe

An audit trail is a chronological record of activities and changes made to data within a system. In Frappe, the audit trail functionality provides a way to track who made what changes, when they were made, and what exactly was modified. This is crucial for:

1. **Compliance**: Meeting regulatory requirements by maintaining detailed change logs
2. **Security**: Detecting unauthorized changes or suspicious activity
3. **Accountability**: Ensuring users are responsible for their actions
4. **Troubleshooting**: Understanding what changed in case of issues
5. **Data Recovery**: Reconstructing previous states of data when needed

Frappe's audit trail capabilities are built into the framework, making it easier for developers to implement comprehensive tracking in their applications.

## Automatic Tracking in Frappe

### Document Version Tracking

By default, Frappe tracks changes to all standard DocType records using the `Version` DocType. Every time a document is created, updated, or deleted, a corresponding version record is created that captures:

- The user who made the change
- The timestamp of the change
- The actual changes made (as a diff)

This version history can be viewed in the "Timeline" section of any document form.

### Document Naming Records

When a document is renamed, Frappe also tracks this change in the `Document Naming Rule` DocType, maintaining a record of previous names and their corresponding new names.

## Configuring Audit Trail

### Track Changes Setting

For each DocType, you can enable or disable change tracking:

1. Navigate to the DocType you want to configure
2. In the "Settings" section, find the "Track Changes" option
3. Enable or disable it as needed

By default, this setting is enabled for most standard DocTypes.

### Track Viewed Setting

Frappe can also track when documents are viewed:

1. Navigate to the DocType you want to configure
2. In the "Settings" section, find the "Track Seen" option
3. Enable or disable it as needed

When enabled, Frappe will record when users view documents of this type.

### Field-level Tracking

For sensitive fields like passwords, tracking can be disabled at the field level:

1. Edit the field definition in the DocType
2. Set the "Track Changes" property to "No"

This ensures that sensitive information doesn't appear in the audit logs.

## Accessing Audit Information

### Timeline View

The most common way to access audit information is through the document's timeline:

1. Open any document
2. Scroll down to the "Timeline" section
3. Look for entries marked with the clock icon ⏱️

Click on these entries to see detailed information about what changed.

### Programmatic Access

You can also access version history programmatically:

```python
import frappe

# Get versions for a specific document
versions = frappe.get_all(
    "Version",
    filters={
        "ref_doctype": "Customer",
        "docname": "CUST-00001"
    },
    fields=["owner", "creation", "data"],
    order_by="creation desc"
)

# Process version data
for version in versions:
    print(f"Changed by {version.owner} on {version.creation}")
    # Version data is stored as a JSON string
    data = frappe.parse_json(version.data)
    print("Changed fields:", list(data.get("changed", [])))
```

### Audit Report

Frappe also provides a built-in "Audit Trail" report:

1. Navigate to "Settings > Audit Trail" or search for "Audit Trail" in the search bar
2. Set filters like date range, user, DocType, etc.
3. Run the report to see a comprehensive view of all changes

## Custom Audit Tracking

### Document Events

For custom audit requirements, you can use document events to implement additional tracking:

```python
# In a custom app's hooks.py
doc_events = {
    "Payment Entry": {
        "on_update": "my_app.events.track_payment_changes",
        "on_cancel": "my_app.events.log_payment_cancellation",
    }
}

# In events.py
def track_payment_changes(doc, method):
    # Custom logging logic here
    frappe.get_doc({
        "doctype": "Custom Audit Log",
        "reference_doctype": doc.doctype,
        "reference_name": doc.name,
        "user": frappe.session.user,
        "timestamp": frappe.utils.now(),
        "action": "Update",
        "details": f"Payment amount changed from {doc.get_doc_before_save().paid_amount} to {doc.paid_amount}"
    }).insert(ignore_permissions=True)
```

### Custom Audit DocType

For more specialized tracking needs, you can create a custom audit DocType:

```python
# Define a custom audit log DocType
custom_audit_log = {
    "doctype": "Custom Audit Log",
    "module": "Core",
    "fields": [
        {
            "fieldname": "reference_doctype",
            "fieldtype": "Link",
            "label": "Reference DocType",
            "options": "DocType",
            "reqd": 1
        },
        {
            "fieldname": "reference_name",
            "fieldtype": "Dynamic Link",
            "label": "Reference Name",
            "options": "reference_doctype",
            "reqd": 1
        },
        {
            "fieldname": "user",
            "fieldtype": "Link",
            "label": "User",
            "options": "User"
        },
        {
            "fieldname": "timestamp",
            "fieldtype": "Datetime",
            "label": "Timestamp"
        },
        {
            "fieldname": "action",
            "fieldtype": "Data",
            "label": "Action"
        },
        {
            "fieldname": "details",
            "fieldtype": "Long Text",
            "label": "Details"
        }
    ]
}
```

## Audit Trail Best Practices

### 1. Enable Tracking Selectively

While tracking changes is important, excessive tracking can impact performance. Enable tracking only for:

- Documents with compliance requirements
- Critical business data
- Sensitive information that needs monitoring

### 2. Implement Custom Field Tracking

For fields that need special attention:

```python
def after_save(doc, method):
    # Check if a sensitive field was changed
    if doc.has_value_changed("credit_limit"):
        frappe.get_doc({
            "doctype": "Custom Audit Log",
            "reference_doctype": doc.doctype,
            "reference_name": doc.name,
            "user": frappe.session.user,
            "timestamp": frappe.utils.now(),
            "action": "Credit Limit Change",
            "details": f"Credit limit changed from {doc._doc_before_save.credit_limit} to {doc.credit_limit}"
        }).insert()
```

### 3. Periodic Audit Review

Implement a regular review process:

1. Schedule weekly/monthly reviews of audit data
2. Create custom reports for specific audit needs
3. Set up alerts for critical changes

### 4. Retention Policy

Implement a retention policy for audit data:

```python
# Scheduled task to clean up old audit records
def cleanup_old_audit_logs():
    # Delete records older than 2 years
    cutoff_date = frappe.utils.add_days(frappe.utils.nowdate(), -730)
    frappe.db.delete(
        "Version", 
        filters={
            "creation": ["<", cutoff_date]
        }
    )
```

## Security Considerations

### Protecting Audit Data

Since audit trails contain sensitive information:

1. **Restrict Access**: Limit who can view the Version DocType
2. **Separate Storage**: For highly sensitive systems, consider storing audit logs in a separate database
3. **Encryption**: Encrypt sensitive fields in audit logs
4. **Immutability**: Ensure audit logs cannot be modified after creation

### Common Vulnerabilities

Be aware of these potential security issues:

1. **Log Injection**: Validate and sanitize data before logging
2. **Excessive Logging**: Don't log sensitive information like passwords
3. **Log Forgery**: Implement mechanisms to verify log integrity

## Conclusion

Frappe's audit trail capabilities provide a robust foundation for tracking and accountability in your applications. By leveraging both built-in features and extending them with custom functionality, you can create a comprehensive audit system that meets your specific business and compliance requirements.