# DocFields in Frappe Framework

DocFields define the fields that make up a DocType. Each field has properties that determine its behavior, appearance, and data handling characteristics.

## Common DocField Properties

### Basic Properties

- **fieldname**: The name used to access the field programmatically. Must be lowercase, no spaces.
- **fieldtype**: The type of field (Data, Link, Select, etc.).
- **label**: The display label shown to users.
- **reqd**: If set to 1, the field becomes mandatory.
- **hidden**: If set to 1, the field is not displayed in the form.
- **read_only**: If set to 1, the field cannot be edited.

### Data Validation

- **options**: Additional configuration specific to the fieldtype:
  - For Link fields: The DocType it links to
  - For Select fields: The list of options (newline separated)
  - For Table fields: The Child DocType
- **default**: The default value for the field.
- **unique**: If set to 1, the field value must be unique across all documents.
- **in_list_view**: If set to 1, the field appears in the list view.
- **in_standard_filter**: If set to 1, the field appears in the standard filters.
- **in_global_search**: If set to 1, the field is included in global search.
- **bold**: If set to 1, the field label appears in bold.
- **precision**: For numeric fields, specifies the number of decimal places.
- **length**: For text fields, specifies the maximum character length.

### Conditional Display

- **depends_on**: A condition that determines when the field is displayed.
  - Example: `depends_on: "eval:doc.status=='Open'"`
- **mandatory_depends_on**: A condition that makes the field mandatory.
  - Example: `mandatory_depends_on: "eval:doc.payment_method=='Credit Card'"`
- **read_only_depends_on**: A condition that makes the field read-only.
  - Example: `read_only_depends_on: "eval:doc.status=='Submitted'"`

### User Experience

- **description**: Additional help text shown below the field.
- **translatable**: If set to 1, the field value can be translated.
- **fetch_from**: Automatically fetch value from a linked document.
  - Example: `fetch_from: "customer.customer_name"`
- **fetch_if_empty**: Only fetch if the field is empty.
- **allow_in_quick_entry**: If set to 1, the field appears in quick entry form.
- **no_copy**: If set to 1, the field value is not copied when duplicating a document.
- **allow_on_submit**: If set to 1, the field can be edited even after document submission.
- **report_hide**: If set to 1, the field is hidden in reports.
- **permlevel**: Permission level for the field (for field-level permissions).
- **ignore_user_permissions**: If set to 1, user permissions are not applied on this field.

## Example DocField JSON

```json
{
  "fieldname": "customer",
  "fieldtype": "Link",
  "label": "Customer",
  "reqd": 1,
  "options": "Customer",
  "description": "Select the customer for this transaction",
  "in_list_view": 1,
  "in_standard_filter": 1,
  "fetch_from": "customer.customer_name",
  "bold": 1
}
```

## Dynamic Behavior

DocFields can have dynamic behavior through client and server scripts. For example:

- Fetching data from other fields or documents
- Validation based on other field values
- Showing or hiding fields based on conditions
- Calculating values automatically

## Best Practices

1. Use clear and descriptive field labels
2. Provide helpful descriptions for complex fields
3. Choose appropriate field types for the data
4. Use validation to ensure data quality
5. Think about the user experience when organizing fields