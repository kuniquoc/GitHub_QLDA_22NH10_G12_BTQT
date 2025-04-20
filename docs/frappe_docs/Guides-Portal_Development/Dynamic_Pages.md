# Dynamic Pages

You can render pages dynamically using the Jinja templating language. To query data, update the `context` object that you pass to the template.

## Example

If you want to show a page listing users, create a `users.html` and `users.py` file in the `www/` folder.

### users.py

```python
import frappe

def get_context(context):
    context.users = frappe.get_list("User", fields=["first_name", "last_name"])
```

### users.html

```html
<h3>List of Users</h3>
<ul>
    {% for user in users %}
        <li>{{ user.first_name }} {{ user.last_name }}</li>
    {% endfor %}
</ul>
```