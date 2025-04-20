# Migrations

Migrations handle database schema changes and data updates during a project's lifecycle. Use `bench migrate` to apply schema changes and data migrations.

## Schema Changes

1. Edit a DocType to add, remove, or change fields.
2. Save the DocType to update its JSON file in the app's source tree.
3. Run `bench migrate` to sync the DocType with the database.

**Note**: Fields are soft-deleted to avoid data loss.

## Data Migrations

1. Write an `execute` function in a Python module.
2. Add the module to `patches.txt` in your app.
3. Alternatively, create a new patch interactively using:

```bash
bench create-patch
```

## One-off Python Statements

Add one-off Python statements in `patches.txt` using the syntax:

```python
execute:{python statement}
```