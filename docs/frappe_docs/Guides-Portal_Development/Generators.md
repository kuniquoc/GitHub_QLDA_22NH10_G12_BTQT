# Generators

If every document in a table (DocType) corresponds to a web page, you can set up generators.

## Steps to Set Up a Generator

1. Add a field `route` that specifies the route of the page.
2. Add a condition field to indicate whether a page is viewable or not.
3. Add the DocType name in `website_generators` in `hooks.py` of your app.
4. Subclass the controller from `frappe.website.website_generator.WebsiteGenerator`.
5. Create a template for your page.
6. Add custom properties (context) for the template.
7. Customize the route and list view.

## Example

### Controller

```python
from frappe.website.website_generator import WebsiteGenerator

class JobOpening(WebsiteGenerator):
    website = frappe._dict(
        template = "templates/generators/job_opening.html",
        condition_field = "published",
        page_title_field = "job_title",
    )

    def get_context(self, context):
        context.title = "Jobs"
        context.introduction = "Current Job Openings"
```

### Template

```html
<h1>{{ job_title }}</h1>
<div>{{ description }}</div>
<a class="btn btn-primary" href="/job_application?job_title={{ doc.job_title }}">Apply Now</a>
```