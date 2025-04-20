# Script Report

You can create tabulated reports using server-side scripts by creating a new Report. Note that Administrator permissions are required for this.

## Steps to Create a Script Report

1. **Create a New Report**
   - Set Report Type as "Script Report".
   - Set "Is Standard" as "Yes".
   - Select the Module in which you want to add this report.
   - In the module folder (e.g., `erpnext/accounts/report/[report-name]`), templates for the report files will be created.

2. **Add Filters**
   - Filters can be added in the `.js` file. Example:

```javascript
frappe.query_reports["Accounts Receivable"] = {
    "filters": [
        {
            "fieldname": "company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_user_default("company")
        }
    ]
};
```

3. **Add the Script**
   - In the `.py` file, add the script for generating the report. Example:

```python
def execute(filters=None):
    columns = [
        {
            "fieldname": "account",
            "label": _("Account"),
            "fieldtype": "Link",
            "options": "Account",
            "width": 300
        },
        {
            "fieldname": "currency",
            "label": _("Currency"),
            "fieldtype": "Link",
            "options": "Currency"
        }
    ]
    data = []
    return columns, data
```

4. **Add a Link for Your Report on the Module Page**
   - Add the report to the module page by updating the `get_data` method in the module's configuration file.