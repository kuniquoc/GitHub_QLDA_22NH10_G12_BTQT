# Request Lifecycle

The Frappe Framework handles different types of requests based on their URL patterns. This document explains the lifecycle of a request and how it is processed.

## Types of Requests

1. **API Requests**:  
   Requests starting with `/api` are handled by the REST API handler.  
   Example: `/api/resource/Task`.

2. **File Downloads**:  
   Requests for file downloads like backups (`/backups`), public files (`/files`), and private files (`/private/files`) are handled separately to respond with a downloadable file.

3. **Web Page Requests**:  
   Requests like `/about` or `/posts` are handled by the website router. These are further explained in this document.

For more details, refer to the documentation on [API Requests](https://docs.frappe.io/framework/user/en/api/rest) and [Static Files](https://docs.frappe.io/framework/user/en/api/static-files).

---

## Request Pre-Processing

Before routing rules are triggered, the following pre-processing steps occur:

1. **Request Initialization**:  
   The request is initialized, and necessary context is set up.

2. **Recorder and Rate Limiter**:  
   The recorder and rate limiter are initialized to monitor and control the request flow.

---

## Path Resolver

Once the request reaches the website router from `app.py`, it is passed through the path resolver. The path resolver performs the following operations:

### Redirect Resolution

The path resolver checks for any possible redirects for the incoming request path. Redirect rules are obtained from:

- The `website_redirects` hook.
- Route redirects defined in website settings.

### Route Resolution

If no redirects are found, the path resolver attempts to resolve the route to get the final endpoint. This is based on:

- Rules from the `website/routing/rules` hook.
- Dynamic routes set in documents of DocTypes with `has_web_view` enabled.

---

## Renderer Selection

Once the final endpoint is resolved, it is passed through all available page renderers. The first page renderer to return `True` for the `can_render` method will be used to render the path.

### Adding a Custom Page Renderer

If you have specific requirements not handled by standard page renderers, you can add a custom page renderer via the `page_renderer` hook.

#### Example

In `hooks.py` of your custom app:

```python
page_renderer = "path.to.your.custom_page_renderer.CustomPage"
```

A custom page renderer class must implement two methods: `can_render` and `render`.

#### Example Implementation

```python
from frappe.website.page_renderers.base_renderer import BaseRenderer

class CustomPage(BaseRenderer):
    def can_render(self):
        return True

    def render(self):
        response_html = "Custom Response"
        return self.build_response(response_html)
```

> **Note**: Custom page renderers take priority, and their `can_render` method will be called before standard page renderers.

---

## Standard Page Renderers

The following are the standard page renderers in Frappe:

1. **StaticPage**:  
   Serves static files like PDFs, images, etc., from the `www` folder of any app.

2. **TemplatePage**:  
   Looks up the `www` folder for HTML or markdown files. If the path is a folder, it serves `index.html` or `index.md`.

3. **WebformPage**:  
   Renders web forms from the Web Form list if the request path matches any available Web Form's route.

4. **DocumentPage**:  
   Renders a document template if available in the `/templates` folder of the DocType.

5. **ListPage**:  
   Renders a list template for a DocType if available in the `/templates` folder.

6. **PrintPage**:  
   Renders a print view for a document using the standard print format or a custom print format.

7. **NotFoundPage**:  
   Renders a standard "Not Found" page and responds with a `404` status code.

8. **NotPermittedPage**:  
   Renders a "Permission Denied" page and responds with a `403` status code.

---

## Notes

- The preferred way of serving static files is by adding them to the `public` folder of your Frappe app. This allows NGINX to serve them directly, leveraging compression and caching while reducing latency.
- Custom page renderers can extend standard page renderers to override or use standard functionalities.