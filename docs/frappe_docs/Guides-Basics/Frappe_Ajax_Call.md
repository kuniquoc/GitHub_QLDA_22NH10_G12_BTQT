# Frappe Ajax Call

In Frappe Framework, you can manage ajax calls via `frappe.call`. The `frappe.call` works in an asynchronous manner, i.e., it sends requests and handles responses via a callback mechanism.

## frappe.call Structure

```javascript
frappe.call({
    method: "",
    type: "POST",
    args: {},
    success: function(r) {},
    error: function(r) {},
    always: function(r) {},
    btn: opts.btn,
    freeze: false,
    freeze_message: "",
    async: true,
    url: "" || frappe.request.url,
});
```

### Parameter Description
- **method**: Dotted path to a whitelisted backend method.
- **type**: HTTP request type ("GET", "POST", "PUT", "DELETE"). Default is "POST".
- **args**: Associative array, arguments that will pass with the request.
- **success**: Function parameter, executed after successful execution of the request.
- **error**: Function parameter, executed after request failure.
- **always**: Function parameter, executed in either case.
- **btn**: Object parameter, triggering object.
- **freeze**: Boolean parameter, freezes the instance until it receives a response.
- **freeze_message**: String parameter, message displayed while the screen is in freeze state.
- **async**: Boolean parameter, default is true. To make the call synchronous, set this parameter to false.
- **url**: String parameter, location from where the request is sent.

## How to Use `frappe.call`?

### Calling Standard API

```javascript
frappe.call({
    method: 'frappe.client.get_value',
    args: {
        'doctype': 'Item',
        'filters': {'name': item_code},
        'fieldname': [
            'item_name',
            'web_long_description',
            'description',
            'image',
            'thumbnail'
        ]
    },
    callback: function(r) {
        if (!r.exc) {
            // code snippet
        }
    }
});
```