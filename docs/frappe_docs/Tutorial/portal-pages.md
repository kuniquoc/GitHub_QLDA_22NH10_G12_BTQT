# Portal Pages

## Introduction

Portal Pages, or Web View Pages, are server-rendered pages designed for website visitors who are not logged into the Desk interface. In our Library Management System, we want to allow Library Members to view available Articles through a public website interface without requiring admin access.

## Enabling Web View for Articles

So far, we've been working exclusively with the Desk interface, which is only accessible to administrative users. Let's create a web view for our Articles that library members can access:

1. Go to the Article DocType and scroll down to the **Web View** section
2. Enable the **Has Web View** and **Allow Guest to View** checkboxes
3. Enter `articles` in the **Route** field
4. Add two new fields to the fields table:
   - **Route** (Field Type: Data, Read Only: Yes)
   - **Published** (Field Type: Check)
5. Click on **Save**

The **Published** field will help filter out documents that shouldn't be displayed on the web interface. Without this filter, you might encounter errors when trying to view unpublished content.

## Testing the Web View

After enabling web views for the Article DocType, you can now view each Article on the website without logging into Desk. To test this:

1. Create a new Article or open an existing one
2. Make sure to set the **Published** checkbox to checked
3. You should see a **See on Website** button at the top left of your form
4. Click on it to view the web view of the Article

## Customizing Web View Templates

When you enable web view for a DocType, two HTML template files are automatically generated:
- `article.html`: Template for individual Article view
- `article_row.html`: Template for displaying Articles in list view

These default templates are basic starting points that we can customize to improve the user experience.

### Customizing Individual Article View

Let's edit the `article.html` file to create a more attractive layout for individual Articles. Frappe uses Bootstrap 4 by default for web views, so we can use any valid Bootstrap 4 markup.

Open the file at `apps/library_management/library_management/templates/article.html` and replace its content with:

```html
{% extends "templates/web.html" %}

{% block page_content %}

<div class="row">
    <div class="col-sm-4">
        {% if image %}
        <img class="card-img-top" src="{{ image }}" alt="{{ title }}">
        {% endif %}
    </div>
    <div class="col-sm-8">
        <h1>{{ title }}</h1>
        <p class="lead">By {{ author }}</p>
        <div class="mt-4">
            <div class="mb-3">
                <span class="badge badge-pill badge-primary">
                    {%- if status == 'Available' -%}
                    Available
                    {%- elif status == 'Issued' -%}
                    Issued
                    {%- endif -%}
                </span>
            </div>
            <div class="mb-3">
                <strong>Publisher:</strong> {{ publisher }}<br>
                <strong>ISBN:</strong> {{ isbn }}
            </div>
            <div class="mb-3">
                {{ description }}
            </div>
        </div>
    </div>
</div>

{% endblock %}
```

### Customizing the Articles List View

Now, let's customize the template for the list of Articles. Open the file at `apps/library_management/library_management/templates/article_row.html` and replace its content with:

```html
<div class="card mb-4" style="max-width: 540px;">
    <div class="row no-gutters">
        <div class="col-md-4">
            {% if doc.image %}
            <img class="card-img" src="{{ doc.image }}" alt="{{ doc.name }}">
            {% endif %}
        </div>
        <div class="col-md-8">
            <div class="card-body">
                <h5 class="card-title"><a href="{{ doc.route }}">{{ doc.title }}</a></h5>
                <p class="card-text">By {{ doc.author }}</p>
                <p class="card-text"><small class="text-muted">{{ doc.status }}</small></p>
            </div>
        </div>
    </div>
</div>
```

## Accessing the Web Views

After customizing both templates, you can access the web views in your browser:

- Individual article: `http://library.test:8000/articles/article-name`
- Articles list: `http://library.test:8000/articles`

The Articles list page will show a list of all published Articles, and you can click on any article to view its details.

## Advanced Portal Features

Frappe offers several advanced features for portal pages:

### Context Injection

You can inject additional context variables by creating a context provider function:

```python
def get_context(context):
    context.related_articles = frappe.get_all("Article", 
        filters={"publisher": context.publisher},
        fields=["title", "route", "author"],
        limit=5
    )
    return context
```

### User-specific Content

You can show different content based on user authentication status:

```html
{% if frappe.session.user != 'Guest' %}
    <div class="alert alert-info">
        You are logged in as {{ frappe.session.user }}
    </div>
{% endif %}
```

### Role-based Content

You can show content based on user roles:

```html
{% if frappe.user_has_role('Library Member') %}
    <button class="btn btn-primary">Reserve Article</button>
{% endif %}
```

## Next Steps

In the next tutorial, we'll learn about creating custom reports and dashboards to analyze data in our Library Management System. We'll also explore how to deploy our application to a production environment.