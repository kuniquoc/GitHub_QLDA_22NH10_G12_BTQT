# How To Migrate Doctype Changes To Production

## DocType / Schema Changes

1. In `developer_mode`, `.json` files for each DocType are automatically updated.
2. Use `bench update` or `bench migrate` to apply these changes to the production site's schema.

## Permissions

Permissions do not get updated automatically. To update permissions:

1. Add a new patch in the `patches.txt` of your app.
2. Use the following command in the patch:

```python
execute:frappe.permissions.reset_perms("[doctype]")
```