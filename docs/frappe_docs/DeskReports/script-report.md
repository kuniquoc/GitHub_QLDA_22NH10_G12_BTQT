# Script Report

Script Reports in Frappe allow you to create highly customizable reports using Python scripts. These reports are ideal for scenarios where the built-in Report Builder or Query Reports are insufficient.

---

## Creating a Script Report

1. Enable **Developer Mode**.
2. Type "new report" in the awesomebar and hit enter.
3. Set the following:
   - **Report Type**: "Script Report"
   - **Is Standard**: "Yes"
   - **Module**: Select the module where the report will reside.
4. A folder will be created in the module directory (e.g., `erpnext/accounts/report/[report-name]`).
5. Write your Python script in the generated `{report-name}.py` file.

---

## Writing the Script

The generated `.py` file includes a boilerplate with an `execute` function. This function takes `filters` as input and returns `columns` and `data`.

### Example:
```python
def execute(filters=None):
    columns = [
        {
            'fieldname': 'account',
            'label': _('Account'),
            'fieldtype': 'Link',
            'options': 'Account'
        },
        {
            'fieldname': 'balance',
            'label': _('Balance'),
            'fieldtype': 'Currency'
        }
    ]
    data = [
        {'account': 'Cash', 'balance': 1000},
        {'account': 'Bank', 'balance': 2000}
    ]
    return columns, data
```

---

## Adding Filters

Filters can be defined in the `{report-name}.js` file. These filters will be available in the `execute` method as a dictionary.

### Example:
```javascript
frappe.query_reports['Balance Sheet'] = {
    filters: [
        {
            fieldname: 'company',
            label: __('Company'),
            fieldtype: 'Link',
            options: 'Company',
            default: frappe.defaults.get_user_default('company')
        },
        {
            fieldname: 'periodicity',
            label: __('Periodicity'),
            fieldtype: 'Select',
            options: ['Monthly', 'Quarterly', 'Yearly'],
            default: 'Yearly'
        }
    ]
};
```

---

## Additional Features

- **Chart**: Add a chart configuration to display visual data.
- **Report Summary**: Display key metrics at the top of the report.
- **Custom Columns**: Define columns dynamically in the `execute` function.

---

Was this article helpful? Let us know your feedback!