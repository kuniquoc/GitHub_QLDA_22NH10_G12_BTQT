# Trigger Event On Deletion Of Grid Row

To trigger an event when a row from a Child Table has been deleted (when the user clicks on the delete button), you need to add a handler to the `fieldname_remove` event of the Child Table. Here, `fieldname` is the fieldname of the Child Table in the Parent Table declaration.

## Example

Assume your parent DocType is named `Item` and has a Table Field linked to the `Item Color` DocType with the declaration name `color`. To "catch" the delete event:

```javascript
frappe.ui.form.on('Item Color', {
    color_remove: function(frm) {
        // Your code here
        // If you console.log(frm.doc.color), you will get the remaining color list
    }
});
```

The same process is used to trigger the add event (when the user clicks on the add row button):

```javascript
frappe.ui.form.on('Item Color', {
    color_add: function(frm) {
        // Your code here
    }
});
```

### Notes

- The handling is done on the Child DocType Table (`form.ui.on`) and not on the Parent DocType.