# Adding Custom Button To Form

To create a custom button on your form, you need to edit the JavaScript file associated with your DocType. For example, if you want to add a custom button to the User form, you must edit `user.js`.

## Function Signature for `add_custom_button`

```javascript
frm.add_custom_button(__(buttonName), function() {
    // perform desired action such as routing to new form or fetching etc.
}, __(groupName));
```

### Example: Adding a Button to User Form

Edit `frappe/core/doctype/user/user.js`:

```javascript
frappe.ui.form.on('User', {
    refresh: function(frm) {
        frm.add_custom_button(__('Get User Email Address'), function() {
            frappe.msgprint(frm.doc.email);
        }, __('Utilities'));
    }
});
```

You should see a button on the User form as shown below.