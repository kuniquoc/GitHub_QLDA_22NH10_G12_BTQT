# Why Frappe?

The Frappe Framework is built with a specific philosophy in mind, aiming to be a complete solution for web application development. Here's why you should consider using Frappe:

## Full Stack

Frappe is a full stack framework that provides almost all the components required to build a modern web application:

- Database Object Mapper (ORM)
- Database Schema Migration Tools
- Templated Server-side Rendering
- REST API
- User Role Permission Models
- Routing
- Background Jobs
- Real-time Updates via WebSockets
- Asset Compilation
- Scheduled Jobs
- Email Management
- File Management with Built-in Storage

This comprehensive approach means you don't need to integrate multiple libraries or frameworks, saving both time and effort. What might take days to set up in other frameworks could be accomplished in hours with Frappe.

## Batteries Included

Frappe takes inspiration from frameworks like Django but goes even further by including features "out of the box" that are commonly needed in business applications:

- Role-based User Permission system
- User Management
- Form Validation
- Image and File Handling
- Email Integration
- Task Scheduling
- Real-time Notifications
- Admin Interface
- REST API Generation
- Website Generator
- Blog Engine
- Web Themes
- Chat Integration
- Custom Dashboard Creation

These components are fully customizable and extensible to match your needs.

## Database Driven

Frappe follows a database-driven approach, meaning that a large portion of your application is configured through the database rather than code files. This offers several advantages:

- Faster Development: Create new models (DocTypes) through the UI without writing code
- More Flexibility: Easily customize models by adding or removing fields
- Standardized API: The framework provides a consistent API for all models
- Consistence Interfaces: Form and List views are automatically generated
- Multi-tenant Architecture: Multiple applications can share the same code base

## Convention Over Configuration

Frappe adopts a "convention over configuration" approach, meaning it follows predefined patterns so you don't have to make numerous small decisions. This makes development more predictable and efficient. For example:

- Controllers follow a specific naming convention (e.g., `todo.py` for the `ToDo` DocType)
- Client-side scripts follow corresponding naming patterns
- Models are stored as JSON files
- Database tables are automatically named (e.g., `tabToDo` for the `ToDo` DocType)
- Object methods and properties are named consistently

## Meta-Programming Model

Frappe uses meta-programming to build interfaces and APIs based on declarative models. This means:

- Create a model once, and interfaces are automatically generated
- Changes to the model are reflected across all interfaces
- Less boilerplate code to write and maintain
- Consistent user experience across the application

## Python and JavaScript

Frappe leverages the strengths of both Python and JavaScript:

- Python for the backend: A language known for readability and extensive libraries
- JavaScript for the frontend: For building interactive user interfaces

## Versatile Deployment Options

Frappe applications can be deployed in various ways:

- Self-hosted on your own server
- Cloud-hosted (AWS, Google Cloud, etc.)
- Platform-as-a-Service (PaaS) options

## Open Source

Frappe is fully open source, which means:

- Free to use and modify
- Transparent and secure (code is auditable)
- Community-supported with regular updates
- No vendor lock-in
- Growing ecosystem of apps and extensions

## Active Community

The Frappe community has been growing since 2008, offering:

- Multiple communication channels for support
- Regular contributions from developers worldwide
- Extensive documentation and learning resources
- Real-world applications across various industries

## Proven in Production

Frappe powers ERPNext, one of the most popular open-source ERP systems, which is used by thousands of companies worldwide. This demonstrates the framework's scalability and reliability in production environments.

## Conclusion

Frappe Framework is designed to be a one-stop solution for web application development, particularly for business applications. Its full-stack approach, built-in features, and database-driven architecture make it an excellent choice for developers who want to build robust applications with less code and in less time.