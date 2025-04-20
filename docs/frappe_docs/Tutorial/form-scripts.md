# Form Scripts

## Introduction

Form Scripts are client-side JavaScript code that enhance the user experience of your forms in Frappe. They allow you to add custom functionality, automate repetitive tasks, and create a more interactive interface for your users.

## Enhancing User Experience

In our Library Management System, let's improve the workflow for creating memberships and transactions. Currently, whenever a librarian wants to create a membership for a member or record a transaction, they need to:

1. Go to the respective DocType's list view
2. Create a new document
3. Select the library member
4. Fill in other details
5. Save the document

We can simplify this process by adding custom buttons directly to the Library Member form.

## Adding Custom Buttons

Let's modify the client-side controller for the Library Member DocType. Open the file `library_member.js` and add the following code:

```javascript
frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            });
        });
        
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            });
        });
    }
});
```

After saving this file, refresh your page and open any Library Member form. You should see two new buttons at the top right of the form:

1. **Create Membership**: Clicking this button will open a new Library Membership form with the Library Member field pre-filled.
2. **Create Transaction**: Clicking this button will open a new Library Transaction form with the Library Member field pre-filled.

This small enhancement significantly improves the workflow for librarians, making the process more intuitive and reducing the number of clicks required to perform common tasks.

## Understanding the Code

Let's break down the code to understand what's happening:

- `frappe.ui.form.on('Library Member', { ... })`: This is the main function that attaches event handlers to the Library Member form.
  
- `refresh: function(frm) { ... }`: The `refresh` event is triggered whenever the form is loaded or refreshed. Our code will execute each time this happens.

- `frm.add_custom_button('Create Membership', () => { ... })`: This adds a custom button with the label "Create Membership". The second parameter is a callback function that executes when the button is clicked.

- `frappe.new_doc('Library Membership', { ... })`: This creates a new document of the specified DocType. The second parameter is an object containing default values for the new document.

## More Form Script Capabilities

Form scripts can do much more than just adding buttons. Here are some other common use cases:

- **Field value calculations**: Automatically calculate values based on other fields
- **Field visibility control**: Show or hide fields based on conditions
- **Fetching data from the server**: Make AJAX calls to get data from the server
- **Validations**: Perform client-side validations before submitting the form
- **Custom dialogs**: Create custom popup dialogs for complex interactions

### Example: Field value calculation

```javascript
frappe.ui.form.on('Library Membership', {
    from_date: function(frm) {
        // Calculate to_date as 30 days after from_date
        if (frm.doc.from_date) {
            frm.set_value('to_date', frappe.datetime.add_days(frm.doc.from_date, 30));
        }
    }
});
```

### Example: Conditional field visibility

```javascript
frappe.ui.form.on('Library Transaction', {
    refresh: function(frm) {
        // Show or hide fields based on transaction type
        frm.toggle_display('return_date', frm.doc.type === 'Issue');
    },
    type: function(frm) {
        frm.toggle_display('return_date', frm.doc.type === 'Issue');
    }
});
```

## Child Table Scripts

Form scripts can also be used to enhance the behavior of child tables (tables within forms). The syntax is slightly different:

```javascript
frappe.ui.form.on('Child Table DocType Name', {
    fieldname: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        // Access the child row using the child variable
    }
});
```

## Best Practices for Form Scripts

1. **Keep scripts lightweight**: Heavy scripts can slow down form loading
2. **Handle errors gracefully**: Always include error handling for AJAX calls
3. **Maintain consistency**: Follow consistent naming and coding conventions
4. **Document your code**: Add comments to explain complex logic
5. **Avoid redundancy**: Don't duplicate functionality that already exists in the framework

## Form Scripts API Reference

Frappe provides a rich API for form scripts. Some commonly used methods include:

- `frm.set_value(fieldname, value)`: Set a field's value
- `frm.toggle_display(fieldname, show)`: Show or hide a field
- `frm.toggle_enable(fieldname, enable)`: Enable or disable a field
- `frm.refresh_field(fieldname)`: Refresh a specific field
- `frm.save()`: Save the form
- `frappe.msgprint(message)`: Show a message to the user
- `frappe.throw(error_message)`: Throw an error with a message

For a complete reference of the Form Scripts API, refer to the [official documentation](https://docs.frappe.io/framework/user/en/api/form).

## Next Steps

In the next tutorial, we'll learn how to create Web Portal pages to allow public access to certain parts of our Library Management System.