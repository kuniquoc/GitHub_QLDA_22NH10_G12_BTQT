# Custom Action in Link Field

You can add a new custom link option to the standard link field by defining the function in the namespace `frappe.ui.form.ControlLink.link_options`. In this namespace, you have access to the link field object.

## Adding Custom Option

```javascript
frappe.ui.form.ControlLink.link_options = function(link) {
    return [
        {
            html: "<a>Custom Link Option</a>",
            label: "Custom Link Option",
            value: "custom__link_option",
            action: () => {}
        }
    ];
};
```

Once a function is assigned to `frappe.ui.form.ControlLink.link_options`, the link field will have a new link option.