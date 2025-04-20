# Jinja API

These are the whitelisted methods that Frappe provides to use in Jinja Templates.

## `frappe.format`

### Usage
`frappe.format(value, df, doc)`  
Formats a raw value (stored in the database) to a user-presentable format. For example, convert `2019-09-08` to `08-09-2019`.

#### Example
```jinja
{{ frappe.format('2019-09-08', {'fieldtype': 'Date'}) }}
```

**Output:**
```
08-09-2019
```

---

## `frappe.format_date`

### Usage
`frappe.format_date(date_string)`  
Formats a date into a human-readable long format.

#### Example
```jinja
{{ frappe.format_date('2019-09-08') }}
```

**Output:**
```
September 8, 2019
```

---

## `frappe.get_url`

### Usage
`frappe.get_url()`  
Returns the site URL.

#### Example
```jinja
{{ frappe.get_url() }}
```

**Output:**
```
https://frappe.io
```

---

## `frappe.get_doc`

### Usage
`frappe.get_doc(doctype, name)`  
Returns a document by its name.

#### Example
```jinja
{% set doc = frappe.get_doc('Task', 'TASK00002') %}
{{ doc.title }} - {{ doc.status }}
```

**Output:**
```
Buy Eggs - Open
```

---

## `frappe.get_list`

### Usage
`frappe.get_list(doctype, filters, fields, order_by, start, page_length)`  
Similar to `frappe.get_all` but filters records for the current session user based on permissions.

#### Example
```jinja
{% set tasks = frappe.get_list('Task', filters={'status': 'Open'}, fields=['title', 'due_date'], order_by='due_date asc') %}
{% for task in tasks %}
### {{ task.title }}
Due Date: {{ frappe.format_date(task.due_date) }}
{% endfor %}
```

**Output:**
```
### Redesign Website
Due Date: September 8, 2019
```

---

## `frappe.db.get_value`

### Usage
`frappe.db.get_value(doctype, name, fieldname)`  
Returns a single field value (or a list of values) from a document.

#### Example
```jinja
{% set company_abbreviation = frappe.db.get_value('Company', 'TennisMart', 'abbr') %}
{{ company_abbreviation }}

{% set title, description = frappe.db.get_value('Task', 'TASK00002', ['title', 'description']) %}
### {{ title }}
{{ description }}
```

**Output:**
```
TM
### Buy Eggs
Get eggs from the store.
```

---

## `frappe.db.get_single_value`

### Usage
`frappe.db.get_single_value(doctype, fieldname)`  
Returns a field value from a Single DocType.

#### Example
```jinja
{% set timezone = frappe.db.get_single_value('System Settings', 'time_zone') %}
{{ timezone }}
```

**Output:**
```
Asia/Kolkata
```

---

## `frappe.get_system_settings`

### Usage
`frappe.get_system_settings(fieldname)`  
Returns a field value from System Settings.

#### Example
```jinja
{% if frappe.get_system_settings('country') == 'India' %}
Pay via Razorpay
{% else %}
Pay via PayPal
{% endif %}
```

**Output:**
```
Pay via Razorpay
```

---

## `frappe.get_meta`

### Usage
`frappe.get_meta(doctype)`  
Returns a DocType meta. It contains information like fields, `title_field`, `image_field`, etc.

#### Example
```jinja
{% set meta = frappe.get_meta('Task') %}
Task has {{ meta.fields | len }} fields.
{% if meta.get_field('status') %}
It also has a Status field.
{% endif %}
```

**Output:**
```
Task has 18 fields. It also has a Status field.
```

---

## `frappe.get_fullname`

### Usage
`frappe.get_fullname(user_email)`  
Returns the full name of the user email passed. If the user is not passed, assumes the current logged-in user.

#### Example
```jinja
The fullname of faris@erpnext.com is {{ frappe.get_fullname('faris@erpnext.com') }}
The current logged-in user is {{ frappe.get_fullname() }}
```

**Output:**
```
The fullname of faris@erpnext.com is Faris Ansari
The current logged-in user is John Doe
```

---

## `frappe.render_template`

### Usage
`frappe.render_template(template_name, context)`  
Render a Jinja template string or file with context.

#### Example
```jinja
{{ frappe.render_template('templates/includes/footer/footer.html', {}) }}
{{ frappe.render_template('{{ foo }}', {'foo': 'bar'}) }}
```

**Output:**
```
bar
```

---

## `frappe._`

### Usage
`frappe._(string)` or `_(string)`  
Translates a string.

#### Example
```jinja
{{ _('This string should get translated') }}
```

**Output:**
```
इस तार का अनुवाद होना चाहिए
```

---

## `frappe.session.user`

### Usage
Returns the current session user.

---

## `frappe.session.csrf_token`

### Usage
Returns the current session's CSRF token.

---

## `frappe.form_dict`

### Usage
If the template is being evaluated in a web request, `frappe.form_dict` is a dict of query parameters; otherwise, it is `None`.

---

## `frappe.lang`

### Usage
Returns the current language used by the translation function (two-letter, lowercase code).