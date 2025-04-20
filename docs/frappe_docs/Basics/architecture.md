# Frappe Architecture

Frappe is a full stack web framework that uses Python and MariaDB on the server side and a JavaScript-based front-end. Let's look at the overall architecture and the libraries and frameworks used.

## Technology Stack

### Server Side

The server side is written in Python and is built on the following frameworks:

- **Python**: The core language used in Frappe
- **MariaDB**: The default database
- **Redis**: Used for caching and task queues
- **Node.js**: Used for installing packages and running builds

### Client Side

The client side is built on JavaScript (ECMAScript 6) and uses the following major libraries:

- **jQuery**: Used extensively for DOM manipulation
- **Bootstrap 4**: CSS framework for consistent design across the application
- **Socket.io**: For realtime event communication
- **Moment.js**: For date manipulation
- **Quill.js**: Rich text editor
- **Frappe Charts**: For displaying charts

## System Architecture

### Frappe Apps

A Frappe application is a standard Python application. Its files are stored in the application folder, where the "sites" folder stores site-specific files.

All applications in Frappe are multi-tenant by default. You can host multiple sites each with its own database for different organizations or projects, while sharing the same codebase.

### Standard Library Modules

Frappe comes with several standard modules that help in implementing various features:

- **Core**: The core module handles users, permissions, sessions, and file storage
- **Email**: For sending, receiving, and queuing emails
- **Desk**: The admin UI module
- **Website**: For generating static websites
- **Workflow**: For managing document workflows
- **Printing**: For generating print formats
- **Integrations**: For third-party integrations

### Directory Structure

A standard Frappe App follows this directory structure:

```
frappe_app/
    frappe_app/         # Package
        __init__.py     # Package Init
        modules.txt     # List of Modules
        patches.txt     # List of Patches
        hooks.py        # Hook Declarations
        config/         # Config Files
            desktop.py  # Desktop Icons
        module_name/    # Custom Module
            __init__.py # Package Init
            doctype/    # DocTypes
            page/       # Pages
            report/     # Reports
```

### DocType Architecture

A DocType in Frappe represents a database table and a controller class. Each DocType consists of:

1. **JSON Schema**: Defines the model structure in JSON
2. **Python Controller Class**: Contains business logic and validations
3. **Client Scripts**: JavaScript code that runs on the client-side

#### Controller Methods

The Python controller class for a DocType can have several standard methods that are called during various operations:

```python
class ToDo(Document):
    def validate(self):
        # Validate data before saving
        if self.status == "Open" and self.date < nowdate():
            frappe.throw("Cannot set a past date for an Open todo")

    def before_save(self):
        # Operations before saving
        self.modified_by = frappe.session.user

    def after_save(self):
        # Operations after saving
        frappe.cache().delete_key('all_todos')
```

## Request Flow

### Initialization

When a request is made to a Frappe application, the following steps take place:

1. The WSGI handler initializes the application environment
2. A new request object is created
3. User authentication is performed
4. The request is routed to the appropriate handler

### Request Handlers

Frappe has different types of request handlers:

- **DocType API**: RESTful API for CRUD operations on DocTypes
- **Page Handler**: For serving dynamic pages
- **Web Pages**: For serving dynamic web pages from templates
- **API Methods**: Custom Python functions exposed as API endpoints

### Response Processing

After the handler processes the request, the following steps take place:

1. The response is formatted (HTML, JSON, etc.)
2. Session data is updated
3. Headers are set
4. The response is returned to the client

## Data Model

Frappe uses a document-oriented approach that consists of:

### DocTypes (Models)

Each DocType represents a database table and has:
- Fields (columns)
- Validations
- Permissions
- Business logic

### Documents (Records)

A Document is an instance of a DocType and represents a row in the database table.

### Child DocTypes

Child DocTypes allow for parent-child relationships between DocTypes:

- A Child DocType's table is linked to a parent DocType
- Child records are loaded with the parent
- They provide a way to implement one-to-many relationships

### Single DocTypes

Single DocTypes store only one record, typically used for:

- Site configuration
- Settings
- Preferences

## Conclusion

Frappe provides a complete framework for building web applications with a well-structured architecture. By leveraging both server-side Python and client-side JavaScript, it offers a comprehensive solution for developing complex business applications with minimal code and maximum efficiency.