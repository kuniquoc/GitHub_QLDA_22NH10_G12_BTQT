# Dialogs Types

Frappe provides a group of standard dialogs that are very useful while coding.

## Alert Dialog

Used for showing non-obstructive messages.

### Parameters
- `txt`: The message to be shown in the Alert Dialog.
- `seconds`: The duration that the message will be displayed. Default is 3 seconds.

### Example

```javascript
show_alert('Hi, you have a new message', 5);
```

## Prompt Dialog

Used for collecting data from users.

### Parameters
- `fields`: A list with the field objects.
- `callback`: A function to process the data in the dialog.
- `title`: The title of the dialog.
- `primary_label`: The label of the primary button.

### Example

```javascript
frappe.prompt([
    {'fieldname': 'birth', 'fieldtype': 'Date', 'label': 'Birth Date', 'reqd': 1}
], function(values) {
    show_alert(values, 5);
}, 'Age verification', 'Subscribe me');
```

## Confirm Dialog

Used to get a confirmation from the user before executing an action.

### Parameters
- `message`: The message to display in the dialog.
- `onyes`: The callback on positive confirmation.
- `oncancel`: The callback on negative confirmation.

### Example

```javascript
frappe.confirm(
    'Are you sure to leave this page?',
    function() {
        window.close();
    },
    function() {
        show_alert('Thanks for staying!');
    }
);
```

## Custom Dialog

You can extend and build your own custom dialogs using `frappe.ui.Dialog`.

### Example

```javascript
var d = new frappe.ui.Dialog({
    'fields': [
        {'fieldname': 'ht', 'fieldtype': 'HTML'},
        {'fieldname': 'today', 'fieldtype': 'Date', 'default': frappe.datetime.nowdate()}
    ],
    primary_action: function() {
        d.hide();
        show_alert(d.get_values());
    }
});
d.fields_dict.ht.$wrapper.html('Hello World');
d.show();
```