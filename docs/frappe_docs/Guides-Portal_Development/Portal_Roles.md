# Portal Roles

Roles can be assigned to Website Users, and they will see menus based on their role.

## Features

1. A default role can be set in **Portal Settings**.
2. Each Portal Menu Item can have a role associated with it. Only users with that role can see the menu item.
3. Rules can be set for default roles that will be assigned to users based on conditions.

### Example: Rules for Default Role

If the email address matches a contact ID, set the role to Customer or Supplier:

```python
default_roles = [
    {
        'role': 'Customer',
        'doctype': 'Contact',
        'email_field': 'email_id',
        'filters': {'ifnull(customer, "")': ('!=', '')}
    },
    {
        'role': 'Supplier',
        'doctype': 'Contact',
        'email_field': 'email_id',
        'filters': {'ifnull(supplier, "")': ('!=', '')}
    }
]
```