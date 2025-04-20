# Custom Module Icon

If you want to create a custom icon for your module, you will have to create an SVG file for your module and set the path to this file in the `desktop/config.py` of your app.

## Example

```python
from frappe import _

def get_data():
    return {
        "Frappe Apps": {
            "color": "orange",
            "icon": "assets/frappe/images/frappe.svg",
            "label": _("Frappe.io Portal"),
            "type": "module"
        }
    }
```

The icon is loaded via AJAX the first time and then rendered.