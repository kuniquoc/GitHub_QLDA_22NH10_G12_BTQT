# Field Types in Frappe Framework

Frappe offers a wide range of field types to choose from when defining your DocTypes. Each field type has its own unique properties and use cases.

## Basic Field Types

### Data
A simple text field for storing short strings. Suitable for names, titles, and short textual data.

### Text
A multi-line text field for longer content. Use this for descriptions, addresses, or any paragraph-length content.

### Text Editor
A rich text editor field that allows formatting (bold, italics, lists, etc.). Ideal for content that requires styling.

### Int
Integer field for storing whole numbers.

### Float
Decimal field for storing floating-point numbers.

### Currency
A field specifically designed for currency values. It respects the system's currency formatting.

### Percent
Field for percentage values.

## Date and Time Types

### Date
A field for storing dates.

### Time
A field for storing time values.

### Datetime
Combines date and time into a single field.

## Selection Types

### Select
A dropdown field with predefined options.

```json
{
  "fieldname": "priority",
  "fieldtype": "Select",
  "label": "Priority",
  "options": "Low\nMedium\nHigh"
}
```

### Link
A field that references another DocType. Creates a relationship between documents.

```json
{
  "fieldname": "customer",
  "fieldtype": "Link",
  "label": "Customer",
  "options": "Customer"
}
```

### Dynamic Link
Similar to Link, but the DocType to reference is determined dynamically by another field.

```json
{
  "fieldname": "reference_type",
  "fieldtype": "Link",
  "label": "Reference Type",
  "options": "DocType"
},
{
  "fieldname": "reference_name",
  "fieldtype": "Dynamic Link",
  "label": "Reference Name",
  "options": "reference_type"
}
```

## File and Image Types

### Attach
A field for attaching files.

### Attach Image
A field specifically for uploading and displaying images.

### Signature
A field for capturing signatures.

## Special Types

### Check
A boolean field (true/false, yes/no).

### Password
A field for entering passwords (masked display).

### Read Only
A non-editable field for displaying information.

### Table
A field that contains a list of another DocType (Child Table).

```json
{
  "fieldname": "items",
  "fieldtype": "Table",
  "label": "Items",
  "options": "Sales Invoice Item"
}
```

### Small Text
Similar to Text, but with a smaller display area.

### Code
A field for storing code snippets with syntax highlighting.

### JSON
A field for storing JSON data.

### HTML
A field that renders HTML content.

### Barcode
A field for generating barcode images.

### Geolocation
A field for storing geographical coordinates.

## Section Types

### Section Break
Creates a new section in the form.

### Column Break
Creates a new column within a section.

### Tab Break
Creates a new tab in the form.

## Other Special Types

### Button
Creates a button that can trigger custom actions.

### Image
Displays an image from a URL.

### Heading
Displays a heading text.

### Fold
Creates a foldable section.

### Virtual Field
A field that's computed on the fly and not stored in the database.

## Choosing the Right Field Type

When designing your DocType, choose field types that best represent your data and provide the most appropriate user interface for data entry and display.