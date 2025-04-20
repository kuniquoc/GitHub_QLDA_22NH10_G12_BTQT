# Child DocTypes in Frappe Framework

Child DocTypes are used to store multiple records related to a parent document. They are commonly used for line items in forms like invoices, orders, or any other scenario where you need a one-to-many relationship.

## Creating a Child DocType

When creating a Child DocType, you need to:

1. Set "Is Child Table" to "Yes" in DocType settings
2. Add fields like in any regular DocType
3. Include a link field to the parent DocType (usually automatically added)

## Using Child DocTypes

Child DocTypes are added to the parent DocType using a Table field:

```json
{
  "fieldname": "items",
  "fieldtype": "Table",
  "label": "Items",
  "options": "Sales Invoice Item"
}
```

Where "Sales Invoice Item" is the name of the Child DocType.

## Key Properties of Child DocTypes

- They don't exist independently - they must be attached to a parent
- They don't have their own permissions system
- They are stored in a separate database table with a foreign key to the parent
- They can be accessed through the parent document in code

## Example Parent and Child Structure

### Parent DocType: Sales Invoice

```json
{
  "name": "Sales Invoice",
  "fields": [
    {
      "fieldname": "customer",
      "fieldtype": "Link",
      "label": "Customer",
      "options": "Customer",
      "reqd": 1
    },
    {
      "fieldname": "posting_date",
      "fieldtype": "Date",
      "label": "Date",
      "default": "Today"
    },
    {
      "fieldname": "items",
      "fieldtype": "Table",
      "label": "Items",
      "options": "Sales Invoice Item"
    },
    {
      "fieldname": "total_amount",
      "fieldtype": "Currency",
      "label": "Total Amount",
      "read_only": 1
    }
  ]
}
```

### Child DocType: Sales Invoice Item

```json
{
  "name": "Sales Invoice Item",
  "istable": 1,
  "fields": [
    {
      "fieldname": "item_code",
      "fieldtype": "Link",
      "label": "Item Code",
      "options": "Item",
      "reqd": 1
    },
    {
      "fieldname": "qty",
      "fieldtype": "Float",
      "label": "Quantity",
      "default": 1
    },
    {
      "fieldname": "rate",
      "fieldtype": "Currency",
      "label": "Rate"
    },
    {
      "fieldname": "amount",
      "fieldtype": "Currency",
      "label": "Amount",
      "read_only": 1
    }
  ]
}
```

## Working with Child Tables in Code

### Accessing Child Tables

```python
# In a controller method
def validate(self):
    for item in self.items:  # 'items' is the fieldname of the table field
        item.amount = item.qty * item.rate
    
    self.total_amount = sum(item.amount for item in self.items)
```

### Adding Items Programmatically

```python
# Create a parent document
invoice = frappe.get_doc({
    "doctype": "Sales Invoice",
    "customer": "Customer 1",
    "posting_date": "2023-01-01"
})

# Add items to the child table
invoice.append("items", {
    "item_code": "ITEM-001",
    "qty": 2,
    "rate": 100
})

invoice.append("items", {
    "item_code": "ITEM-002",
    "qty": 1,
    "rate": 200
})

invoice.insert()
```

## Best Practices

1. Keep child tables focused on related data only
2. Use computed fields to show aggregates in the parent
3. Implement validation in both parent and child controllers
4. For large tables, implement pagination or lazy loading
5. Use meaningful field names and ensure proper indexing for performance
6. Consider using read-only fields for derived values instead of storing redundant data