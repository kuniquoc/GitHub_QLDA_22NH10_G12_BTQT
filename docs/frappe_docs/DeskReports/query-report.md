# Query Report

Query Reports in Frappe allow you to create reports using SQL queries. These reports are ideal for scenarios where data can be fetched directly from the database.

---

## Creating a Query Report

1. Type "new report" in the awesomebar and hit enter.
2. Set the following:
   - **Report Type**: "Query Report"
   - **Is Standard**: "Yes"
   - **Module**: Select the module where the report will reside.
3. Write your SQL query in the **Query** field.

---

## Writing the Query

The SQL query must include the `LIMIT %(start)s, %(page_length)s` clause for pagination. You can use filters as variables in the query.

### Example:
```sql
SELECT
    name,
    customer_name,
    grand_total
FROM
    `tabSales Invoice`
WHERE
    posting_date BETWEEN %(from_date)s AND %(to_date)s
```

---

## Adding Filters

Filters can be defined in the `{report-name}.js` file. These filters will be passed as parameters to the SQL query.

### Example:
```javascript
frappe.query_reports['Sales Invoice Report'] = {
    filters: [
        {
            fieldname: 'from_date',
            label: __('From Date'),
            fieldtype: 'Date',
            default: frappe.datetime.add_months(frappe.datetime.nowdate(), -1)
        },
        {
            fieldname: 'to_date',
            label: __('To Date'),
            fieldtype: 'Date',
            default: frappe.datetime.nowdate()
        }
    ]
};
```

---

Was this article helpful? Let us know your feedback!