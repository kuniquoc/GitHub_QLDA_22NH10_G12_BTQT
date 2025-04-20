# Report Print Formats

In version 4.1, Report Print Formats were introduced. These are HTML templates that you can use to format Query Report data for printing.

## Creating New Print Formats

To create a new Print Format, drop a `.html` file in the folder of the query report. For example, for the General Ledger report, create a `general_ledger.html` file alongside the `.js` and `.py` files.

### Example Directory Structure

```
erpnext/accounts/general_ledger/
├── __init__.py
├── general_ledger.html
├── general_ledger.js
├── general_ledger.json
└── general_ledger.py
```

## Templating

For templating, an adapted version of John Resig's microtemplating script is used. Data is available to the template as:

- `data`: A list of records, with each record as an object with slugified properties from labels.
- `filters`: Filters set in the report.
- `report`: The report view object.

### Example

Here is how the General Ledger Report is built:

```html
<div>
    <h1>General Ledger</h1>
    <table>
        <thead>
            <tr>
                <th>Date</th>
                <th>Account</th>
                <th>Debit</th>
                <th>Credit</th>
            </tr>
        </thead>
        <tbody>
            <% for (var i = 0; i < data.length; i++) { %>
                <tr>
                    <td><%= data[i].posting_date %></td>
                    <td><%= data[i].account %></td>
                    <td><%= data[i].debit %></td>
                    <td><%= data[i].credit %></td>
                </tr>
            <% } %>
        </tbody>
    </table>
</div>
```