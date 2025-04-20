# Overriding Link Query By Custom Script

You can override the standard link query by using `set_query` via the Client Script DocType from the desk.

## Method Formats

- `set_query(field_name, options_function())` for regular fields.
- `set_query(field_name, child_table_name, options_function())` for fields in child tables.

## Adding Filters

You can add filters to the query:

```javascript
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm) {
    frm.set_query("bank_account", function() {
        return {
            "filters": {
                "account_type": "Bank",
                "group_or_ledger": "Ledger"
            }
        };
    });
});
```

### More Complex Query

```javascript
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm) {
    frm.set_query("bank_account", function() {
        return {
            "filters": [
                ["Bank Account", "account_type", "=", "Bank"],
                ["Bank Account", "group_or_ledger", "!=", "Group"]
            ]
        };
    });
});
```

## Calling a Different Method to Generate Results

You can also set a server-side method to be called on the query:

```javascript
frm.set_query("item_code", "items", function() {
    return {
        query: "erpnext.controllers.queries.item_query",
        filters: frm.doc.enquiry_type === "Maintenance" ?
            {"is_service_item": "Yes"} : {"is_sales_item": "Yes"}
    };
});
```