# Form & View Settings in Frappe Framework

Frappe provides various settings to customize how forms and views appear and behave. These settings control the presentation of your DocTypes in the user interface.

## Form Settings

### Basic Form Settings

- **Hide Toolbar**: Hides the toolbar in the form view.
- **Hide Sidebar**: Hides the sidebar in the form view.
- **Allow Print**: Allows printing of the document.
- **Allow Email**: Allows emailing the document.
- **Allow Copy**: Allows creating a duplicate of the document.
- **Allow Rename**: Allows renaming the document.
- **Allow Import**: Allows importing documents of this type.
- **Track Changes**: Tracks changes made to the document.
- **Track Views**: Tracks when the document is viewed.
- **Quick Entry**: Enables quick entry form.

### Image Fields

- **Image Field**: Specifies which field contains the image to display in list views and cards.
- **Image View**: If enabled, shows the document as an image card in list view.

### Title & Search

- **Title Field**: Specifies which field should be used as the document title.
- **Search Fields**: Comma-separated list of fields to search when using the search function.
- **Default Sort Field**: Field used for default sorting.
- **Default Sort Order**: ASC or DESC.

## List View Settings

- **List Title Field**: Field to use as the title in list view.
- **Image Field**: Field to use for images in list view.
- **Default View**: Default view type (List, Report, Calendar, etc.).
- **Default Filters**: JSON string of default filters to apply in list view.

## Calendar View Settings

- **Calendar Name Field**: Field to be shown in the calendar (e.g., title).
- **Calendar Date Field**: Date field to be used for positioning in calendar.
- **Start Date Field**: For events with duration.
- **End Date Field**: For events with duration.

## Kanban View Settings

- **Kanban Column Field**: Field used to group items in Kanban view.
- **Kanban WIP Limit**: Work in progress limit for Kanban columns.

## Example Settings Configuration

```json
{
  "title_field": "customer_name",
  "search_fields": "customer_name,contact_no,email_id",
  "image_field": "customer_image",
  "default_print_format": "Standard Invoice Format",
  "allow_copy": 1,
  "allow_rename": 1,
  "quick_entry": 1,
  "track_changes": 1
}
```

## Form Layout

Form layout is determined by how you organize your fields with Section Breaks, Column Breaks, and Tab Breaks:

- **Section Break**: Creates a new section in the form.
- **Column Break**: Splits a section into multiple columns.
- **Tab Break**: Creates a new tab in the form.

## Conditional Display

You can conditionally show or hide fields based on the values of other fields:

```json
{
  "fieldname": "credit_card_number",
  "fieldtype": "Data",
  "label": "Credit Card Number",
  "depends_on": "eval:doc.payment_method=='Credit Card'"
}
```

## Best Practices

1. Use appropriate break fields to create a logical form layout
2. Group related fields together in sections or tabs
3. Use conditional display to simplify forms by showing only relevant fields
4. Choose meaningful title and search fields for easy document discovery
5. Configure image fields appropriately for visual identification
6. Leverage quick entry for frequently created documents with minimal required fields