# DocTypes

## Introduction to DocTypes

DocTypes (Document Types) are the core building blocks of any application built on the Frappe Framework. They represent a database table and its associated business logic combined into a single entity. Think of a DocType as:

1. A **data model** that defines fields, validations, and relationships
2. A **form interface** for creating and editing records
3. A **controller class** containing business logic and methods
4. A **set of permission rules** defining access control
5. An **API endpoint** for programmatic interaction

DocTypes form the foundation of data modeling in Frappe applications and are used to create everything from simple form entries to complex business objects.

## DocType Components

A DocType consists of several key components:

### Schema Definition (JSON)

The schema defines the structure of the DocType, including its fields and properties. It's stored as a JSON file.

```json
{
  "name": "Customer",
  "doctype": "DocType",
  "module": "CRM",
  "naming_rule": "By fieldname",
  "naming_field": "customer_name",
  "fields": [
    {
      "fieldname": "customer_name",
      "fieldtype": "Data",
      "label": "Customer Name",
      "reqd": 1
    },
    {
      "fieldname": "contact_details_section",
      "fieldtype": "Section Break",
      "label": "Contact Details"
    },
    {
      "fieldname": "email",
      "fieldtype": "Data",
      "label": "Email",
      "options": "Email"
    },
    {
      "fieldname": "phone",
      "fieldtype": "Data",
      "label": "Phone",
      "options": "Phone"
    }
  ]
}
```

### Controller Class (Python)

The controller contains the business logic for the DocType. It's a Python class that inherits from the `Document` class.

```python
class Customer(Document):
    def validate(self):
        # Validate email format
        if self.email and not validate_email_format(self.email):
            frappe.throw("Invalid email format")
    
    def before_save(self):
        # Convert customer name to title case
        self.customer_name = self.customer_name.title()
    
    def after_insert(self):
        # Send welcome email
        send_welcome_email(self)
```

### Client Scripts (JavaScript)

Client scripts add client-side behaviors to the form interface of a DocType.

```javascript
frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        // Add custom button
        frm.add_custom_button('Send Welcome Email', function() {
            frappe.call({
                method: 'my_app.api.send_welcome_email',
                args: {
                    customer: frm.doc.name
                },
                callback: function(r) {
                    frappe.show_alert('Email sent successfully');
                }
            });
        });
    },
    
    phone: function(frm) {
        // Auto format phone number
        frm.set_value('phone', format_phone_number(frm.doc.phone));
    }
});
```

### Permissions

Permissions define who can access and perform actions on the DocType. They are defined in the DocType settings.

## Field Types

DocTypes support various field types to represent different kinds of data:

### Basic Field Types

- **Data**: For short text strings
- **Text**: For longer text content
- **Int**: For integer values
- **Float**: For decimal numbers
- **Date**: For date values
- **Time**: For time values
- **Datetime**: For date and time values
- **Check**: For boolean (true/false) values
- **Select**: For dropdown options
- **Link**: For references to other DocTypes
- **Table**: For child tables with multiple rows
- **Attach**: For file attachments
- **Image**: For image attachments

### Layout Field Types

- **Section Break**: Creates a new section in the form
- **Column Break**: Creates a new column within a section
- **Tab Break**: Creates a new tab in the form
- **HTML**: For custom HTML content

### Special Field Types

- **Signature**: For capturing signatures
- **Barcode**: For generating and storing barcodes
- **Geolocation**: For storing geographical coordinates
- **Password**: For storing encrypted passwords
- **Color**: For selecting and storing colors

## DocType Features

### Naming

DocTypes can have different naming rules:

- **Auto-increment**: Sequential numbers (e.g., CUST-00001)
- **By field**: Use a specific field's value as the document name
- **By naming series**: Configurable naming patterns
- **Random string**: Generated random IDs
- **By script**: Custom naming via a script

### Document Status

Documents can have different states:

- **Draft**: Initial state
- **Submitted**: Confirmed state
- **Cancelled**: Invalidated state

### Document Versioning

Frappe maintains version history of all document changes, allowing you to:
- Track who made changes
- See what was changed
- Restore previous versions if needed

### Workflow

DocTypes can have workflows defined with:
- States (e.g., Draft, Approved, Rejected)
- Transitions between states
- Role-based permissions for transitions

## Creating and Managing DocTypes

### Creating a DocType

DocTypes can be created in two ways:

1. **Using the Desk UI**:
   - Go to "Developer > DocType > New"
   - Configure fields and settings
   - Save the DocType

2. **Via Code**:
   - Create a JSON file defining the DocType
   - Create Python controller class
   - Create client scripts

### Customizing DocTypes

Existing DocTypes can be customized without modifying the source code:

- Add custom fields
- Hide or make fields mandatory
- Change field labels and descriptions
- Add custom scripts
- Create custom forms

## Types of DocTypes

### Standard DocType

The default type, creating a normal database table with multiple records.

### Single DocType

Creates a single record that's typically used for settings or configurations.

### Child DocType

Used as a table field within another DocType for one-to-many relationships.

## DocType Relationships

DocTypes can be related to each other in several ways:

### Link Fields

A link field creates a reference to another DocType, similar to a foreign key in databases.

```json
{
  "fieldname": "customer",
  "fieldtype": "Link",
  "label": "Customer",
  "options": "Customer"
}
```

### Table Fields

A table field creates a child table linked to another DocType (which must be a Child DocType).

```json
{
  "fieldname": "items",
  "fieldtype": "Table",
  "label": "Items",
  "options": "Sales Invoice Item"
}
```

### Dynamic Links

A dynamic link allows referencing documents from multiple DocTypes.

```json
{
  "fieldname": "reference_doctype",
  "fieldtype": "Link",
  "label": "Reference DocType",
  "options": "DocType"
},
{
  "fieldname": "reference_name",
  "fieldtype": "Dynamic Link",
  "label": "Reference Name",
  "options": "reference_doctype"
}
```

## Best Practices for DocTypes

1. **Plan your data model**: Design your DocTypes with relationships in mind
2. **Use meaningful names**: Use clear, descriptive names for DocTypes and fields
3. **Use field validations**: Add appropriate validations to ensure data integrity
4. **Implement business logic in controllers**: Keep complex logic in the Python controller
5. **Add appropriate permissions**: Configure permissions based on roles
6. **Document relationships**: Use Link fields to establish relationships between DocTypes
7. **Leverage standard features**: Use built-in features like naming series and workflows
8. **Think about user experience**: Design fields and layout with the end user in mind

## Conclusion

DocTypes are the cornerstone of Frappe applications, providing a powerful way to model data, implement business logic, and create user interfaces. Understanding how to design and use DocTypes effectively is essential for developing robust applications on the Frappe Framework.