# Single DocType in Frappe Framework

A Single DocType is a DocType that has only one instance in the database. It is useful for persisting things like System Settings, which don't make sense to have multiple records.

## Creating a Single DocType

When creating a DocType in Frappe, you can set it as a Single DocType by checking the "Is Single" option in the DocType form.

## Accessing Single DocTypes

Since there's only one instance of a Single DocType, you can directly fetch it using `get_doc` without specifying a name:

```python
settings = frappe.get_doc('System Settings')
settings.notification_frequency  # 'Daily'
```

To update a Single DocType, you can modify its properties and save it:

```python
settings = frappe.get_doc('System Settings')
settings.notification_frequency = 'Weekly'
settings.save()
```

## Schema

Single DocTypes are stored in the `tabSingles` table in the database, with each property having its own record.

The table has the following columns:
- `doctype`: The name of the DocType
- `field`: The fieldname
- `value`: The value of the field

## Use Cases

Single DocTypes are commonly used for:

1. **System Settings**: Configuration settings that apply to the entire system
2. **Company Information**: Details about the company like name, address, logo, etc.
3. **Email Settings**: SMTP server configuration
4. **Print Settings**: Default paper size, margins, etc.
5. **Feature Flags**: Enabling/disabling features across the application

## Example Single DocType: Website Settings

```json
{
  "name": "Website Settings",
  "is_single": 1,
  "fields": [
    {
      "fieldname": "website_title",
      "fieldtype": "Data",
      "label": "Website Title"
    },
    {
      "fieldname": "website_description",
      "fieldtype": "Text Editor",
      "label": "Website Description"
    },
    {
      "fieldname": "website_logo",
      "fieldtype": "Attach Image",
      "label": "Website Logo"
    },
    {
      "fieldname": "enable_view_tracking",
      "fieldtype": "Check",
      "label": "Enable View Tracking"
    }
  ]
}
```

## Best Practices

1. Use Single DocTypes only for settings or configurations that should have a single instance
2. Keep the fields focused on a specific area of functionality
3. Use appropriate fieldtypes for better user experience
4. Consider adding doctype-level permissions to control who can modify these settings
5. For complex settings, organize fields into logical sections using Section Breaks