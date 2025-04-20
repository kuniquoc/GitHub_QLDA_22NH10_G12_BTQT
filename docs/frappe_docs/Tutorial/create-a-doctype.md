# Create a DocType

## Introduction

A DocType in Frappe Framework is analogous to a Model in other frameworks. It defines not only the properties of the Model but also its behavior. In this tutorial, we will create our first DocType for the Library Management application that we've been building.

## Enable Developer Mode

Before we create DocTypes, we need to enable developer mode on our bench. This will allow us to track DocTypes into version control with our app.

From your `frappe-bench` directory, run the following command:

```bash
$ bench set-config -g developer_mode true
$ bench start
```

## Creating a DocType

1. In the Desk interface, navigate to the **DocType List** using the Awesomebar (the search bar at the top).
2. Click on the **New** button to create a new DocType.

For our Library Management app, we will start by creating an **Article** DocType:

3. Fill in the following details:
   - **Name**: Article
   - **Module**: Library Management

4. Add the following fields in the Fields table:
   - **Article Name** (Field Type: Data, Mandatory: Yes)
   - **Image** (Field Type: Attach Image)
   - **Author** (Field Type: Data)
   - **Description** (Field Type: Text Editor)
   - **ISBN** (Field Type: Data)
   - **Status** (Field Type: Select, Options: Issued and Available)
   - **Publisher** (Field Type: Data)

5. Make sure the "Custom?" checkbox is unchecked so that boilerplate code will be generated for this DocType.

6. Click on **Save**.

Once saved, you will see a **Go to Article List** button at the top right corner of the form. Click on it to go to the Article List, which will be empty since we haven't created any records yet.

## Creating Records

Before creating records, we need to clear the Desk cache:

1. Click on the **Settings** dropdown on the right side of the navbar
2. Select **Reload**

Now, you should be able to see the **New** button in the Article List. Click on it, fill in the form for your first Article, and click **Save**.

## What Happens When You Create a DocType?

When you create a DocType, several things happen behind the scenes:

### 1. Database Table

A database table with the name `tabArticle` is created with the fields we specified. Field names are converted from Title Case to snake_case automatically. For example, "Article Name" becomes `article_name` in the database.

Besides the fields we defined, the system also creates standard fields like:
- `name`: Primary key column
- `creation`: Timestamp when record was created
- `modified`: Timestamp when record was last modified
- `modified_by`: User who last modified the record
- `owner`: User who created the record
- `docstatus`: Document status (0 for draft, 1 for submitted, 2 for cancelled)
- Other fields for parent-child relationships

You can verify the table structure by running SQL commands in the MariaDB console:

```sql
DESC tabArticle;
SELECT * FROM tabArticle;
```

### 2. Desk Views

The system automatically creates different views for your DocType:
- **List View**: Shows all records in a table format
- **Form View**: Used for creating new records or editing existing ones

### 3. Form Layout

The layout of fields in the Form View follows the order you defined in the Fields table when creating the DocType.

### 4. Boilerplate Code

When developer mode is enabled and you create a DocType, several files are generated in your app directory:

```
library_management/library_management/doctype/article/
├── __init__.py
├── article.js      # Client-side controller for Form view
├── article.json    # JSON file defining DocType attributes
├── article.py      # Python controller for Article
└── test_article.py # Python Unit Test boilerplate
```

These files are created at:
```
apps/library_management/library_management/library_management/doctype/article/
```

You can check these newly created files by running:

```bash
$ cd apps/library_management
$ git status -u
```

## Next Steps

Now that we have created our first DocType, we can proceed with creating more DocTypes for our Library Management application. In the next tutorial, we will explore the features of DocTypes in more detail.

Remember, a DocType is more than just a database table. It's a complete abstraction that includes:
- The database table and its schema
- The form layout for manipulating records
- Various views like List, Form, etc.
- Client and server-side controllers
- Permissions and access levels

Let's continue building our application in the next section.