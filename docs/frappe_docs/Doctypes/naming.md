# Document Naming in Frappe Framework

Every document in Frappe needs a unique identifier called `name`. The framework provides several ways to control how document names are generated.

## Naming Options

When creating a DocType, you can specify how documents should be named using the `Autoname` field:

### field:[fieldname]

Uses the value of the specified field as the document name.

```
field:customer_name
```

### naming_series:

Uses a naming series pattern defined in the document. You must include a `naming_series` field in your DocType.

```
naming_series:
```

With a field like:

```json
{
  "fieldname": "naming_series",
  "fieldtype": "Select",
  "label": "Series",
  "options": "ACC-SINV-.YYYY.-\nACC-SINV-\nS-",
  "default": "ACC-SINV-.YYYY.-"
}
```

### [series]

Directly define a naming series pattern in the `Autoname` field.

```
INV-.YYYY.-.MM.-.#####
```

### Prompt

Asks the user to enter a name when creating a new document.

```
Prompt
```

### hash

Generates a random hash as the document name.

```
hash
```

### format:###

Uses a custom format string with field values.

```
format:PRE-{customer_name}-{date}
```

## Naming Series Patterns

### Date Formats

- `.YYYY.` - 4-digit year (2023)
- `.YY.` - 2-digit year (23)
- `.MM.` - 2-digit month (01-12)
- `.DD.` - 2-digit day (01-31)

### Number Series

- `#` - Single digit
- `####` - Multiple digits with leading zeros

For example, `INV-YYYY-####` might generate `INV-2023-0001`.

## Setting a Custom Name

You can also override the automatic naming by implementing a custom naming function in your DocType controller:

```python
def autoname(self):
    # Custom naming logic
    self.name = f"CUST-{self.customer_code}-{frappe.utils.now_datetime().strftime('%Y%m')}"
```

## Best Practices

1. Choose a naming scheme that makes documents easily identifiable
2. Consider including date components for chronological sorting
3. Use prefixes to distinguish between different types of documents
4. Keep names reasonably short while still being descriptive
5. Ensure names will remain unique even with high document volumes