# Client Script

A **Client Script** lets you dynamically define a custom Form Script that is executed on a user's browser. It allows you to customize the behavior of forms and fields in Frappe.

---

## How to Create a Client Script

1. Ensure your role is **System Manager**.
2. Type "New Client Script" in the awesomebar and hit enter to create a new Client Script document.
3. Select the **DocType** whose form you wish to customize.
4. Update the script using the preset template and save.
5. Head over to the DocType you've customized and see the changes.

---

## Features

- Utilize all JavaScript APIs, along with Frappe's APIs.
- Add custom validations, fetch values, customize field properties, and more.
- Scripts are executed only in the browser and do not affect API or backend operations.

---

## Examples

### 1. Custom Validation
Add additional form validations while creating or updating a document:
```javascript
frappe.ui.form.on('Task', 'validate', function(frm) {
    if (frm.doc.from_date < get_today()) {
        msgprint('You cannot select a past date in From Date');
    }
});
```

### 2. Fetching Values on Field Updates
Fetch `local_tax_no` when the `customer` field is updated:
```javascript
cur_frm.add_fetch('customer', 'local_tax_no', 'local_tax_no');
```

### 3. Customize Field Properties
Make a field read-only after saving:
```javascript
frappe.ui.form.on('Task', {
    refresh: function(frm) {
        frm.set_df_property('ibsn', 'read_only', !frm.is_new());
    }
});
```

### 4. Calculate Incentives
Calculate sales incentives on a Sales Invoice form:
```javascript
frappe.ui.form.on('Sales Invoice', {
    validate: function(frm) {
        total_incentive = 0;
        $.each(frm.doc.sales_team, function(i, d) {
            let incentive_percent = 2;
            if (frm.doc.base_grand_total > 400) incentive_percent = 4;
            d.incentives = flt(frm.doc.base_grand_total) * incentive_percent / 100;
            total_incentive += flt(d.incentives);
        });
        frm.doc.total_incentive = total_incentive;
    }
});
```

---

Was this article helpful? Let us know your feedback!