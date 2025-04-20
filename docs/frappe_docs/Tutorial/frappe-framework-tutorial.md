# Frappe Framework Tutorial

## Introduction
This guide aims to teach you how to create a web application from scratch using the Frappe Framework.

## Who is this for?
This guide is intended for software developers who are familiar with how web applications are built. The Frappe Framework is powered by Python, JavaScript and Redis, to name a few technologies and supports MariaDB and PostgreSQL databases. Jinja is used as the templating engine for Web Views and Print formats. Redis is used for caching, maintaining job queues and realtime updates.

Frappe Framework and the apps you build on it require `git` for version control and update management via Bench. It is also expected that you are familiar with basic git commands.

## What are we building?
We will build a simple **Library Management System** in which the **Librarian** can log in and manage Articles and Memberships. We will build the following models:

1. **Article**: A Book or similar item that can be rented.
2. **Library Member**: A user who is subscribed to a membership.
3. **Library Transaction**: An Issue or Return of an article.
4. **Library Membership**: A document that represents an active membership of a Library Member.
5. **Library Settings**: Settings that define values like Loan Period and the maximum number of articles that can be issued at a time.

The Librarian will log in to an interface known as **Desk**, a rich admin interface that ships with the framework. The Desk provides many standard views like List view, Form view, Report view, etc, and many features like Role-based Permissions.

We will also create public Web Views which can be accessed by the Library Members where they can browse available Articles.

## Table of Contents
1. Create a Bench
2. Create an App
3. Create a Site
4. Create a DocType
5. DocType Features
6. Controller Methods
7. Types of DocType
8. Form Scripts
9. Portal Pages
10. Additional Resources

## Notes
This tutorial is based on the Frappe Framework documentation available at https://docs.frappe.io/framework/user/en/tutorial. The tutorial walks through building a complete Library Management System application using the Frappe Framework.

Follow the sections in order to progressively build your application, starting from setting up your development environment with Bench, to creating DocTypes for your data models, implementing controller logic, and finally creating web views for end users.