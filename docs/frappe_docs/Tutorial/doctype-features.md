# DocType Features

## Introduction

In the previous chapter, we created the Article DocType. Now let's explore more features that we can customize to enhance our DocType.

## Naming

When you created a document with the Form earlier, you might have noticed that the `name` value of the document was a randomly generated hash. Let's change this so that the Article Name we provide becomes the `name` of the document.

To configure this:

1. Open the DocType list from the search bar and click on **Article**
2. Scroll down to the **Naming** section 
3. In the **Auto Name** field, enter `field:article_name`
4. Click on **Save**

Now, go back to the Article List and create a new article. The `name` of the document will now be the Article Name you enter, and it must be unique across all Articles. This means you cannot create another article with the same name.

You can verify this change by running a select query in the MariaDB console:

```sql
SELECT * FROM tabArticle;
```

There are various other naming options available in Frappe:

- `field:[fieldname]`: Use the value of the specified field as the name
- `naming_series:`: Use the naming series pattern
- `[prefix]####`: Auto-incremented number with prefix
- `[prefix]####[suffix]`: Auto-incremented number with prefix and suffix
- `[expression]`: Evaluate an expression to generate a name

## Form Layout

The layout of fields in a form can be customized to make better use of available space. Let's enhance our Article DocType's form layout:

1. Go to the Article DocType 
2. Scroll to the **Fields** section
3. Add two new fields:
   - A **Column Break** after a few fields to create two columns
   - A **Section Break** to separate groups of fields

Additionally, you can hide fields that don't need to be shown in the form directly.

### Form Settings

The Form Settings section provides more options to customize the form:

1. Go to the Article DocType and scroll down to the **Form Settings** section
2. Enter `image` in the **Image Field** input. This will display the image at the top left of the form
3. Enable **Allow Rename** to allow users to rename documents after creation

## Permissions

Frappe provides a comprehensive role-based permission system. You can configure which roles are allowed to perform specific actions on a DocType:

1. Go to the Article DocType
2. Scroll down to the **Permission Rules** section
3. Add permission rules for different roles:
   
   - Add a **Librarian** role with permissions for all actions (Read, Write, Create, Delete, Submit, Cancel, Amend)
   - Add a **Library Member** role with permission only for the **Read** action

You can test these permissions by:
1. Creating new Users and assigning them the respective roles
2. Logging in with each user to see what actions they can perform

This role-based permission system ensures that users can only perform actions appropriate to their role within the system.

## Other DocType Features

Frappe offers many more features for customizing DocTypes:

- **Document States**: Define different states for your documents (Draft, Submitted, Cancelled)
- **Linked DocTypes**: Create relationships between different DocTypes
- **Child Tables**: Add tables within forms for one-to-many relationships
- **Validation & Business Logic**: Write custom validation and business logic in controller methods
- **Workflow**: Define approval workflows for documents
- **Events & Hooks**: Trigger custom code on document events

## Next Steps

In the next tutorial, we'll explore how to add controller methods to our DocType to implement custom business logic.

Remember that DocTypes are the building blocks of your Frappe application. Taking time to properly configure them will result in a more intuitive and efficient user experience.