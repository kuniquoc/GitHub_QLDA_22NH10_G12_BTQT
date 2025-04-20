# Controller Methods

## Introduction

Controller methods allow you to write business logic that executes during the lifecycle of a document. In this tutorial, we will learn how to implement controller methods by creating our second DocType: Library Member.

## Creating the Library Member DocType

First, let's create the Library Member DocType with the following fields:

1. **First Name** (Field Type: Data, Mandatory: Yes)
2. **Last Name** (Field Type: Data)
3. **Full Name** (Field Type: Data, Read Only: Yes)
4. **Email Address** (Field Type: Data)
5. **Phone** (Field Type: Data)

Follow these steps:
1. Navigate to the DocType List using the Awesomebar
2. Click on New
3. Set Name as "Library Member" and select "Library Management" as the Module
4. Add the fields as specified above
5. Save the DocType

After creating the DocType, go to the Library Member list, clear the cache from **Settings > Reload**, and try to create a new Library Member.

You'll notice that the Full Name field is not shown in the form. This is because we set it as Read Only. It will only be displayed when it has a value.

## Adding Controller Logic

Now, let's add controller logic to automatically compute the Full Name from First Name and Last Name. This is where controller methods come in handy.

Open your code editor and navigate to the Python controller file for Library Member. The file path should be:

```
apps/library_management/library_management/library_management/doctype/library_member/library_member.py
```

Edit the file to implement the `before_save` method:

```python
class LibraryMember(Document):
    # this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
```

This code uses the `before_save` hook, which runs every time a document is saved. It sets the `full_name` field by combining `first_name` and `last_name`.

> **Note**: If the above snippet doesn't work for you, make sure server side scripts are enabled, and then restart bench:
> ```bash
> $ bench set-config -g server_script_enabled true
> ```

## Testing the Controller

After implementing the controller method:

1. Go back to the Library Member list
2. Create a new Library Member
3. Fill in the First Name and Last Name fields
4. Save the document

You should now see the Full Name field populated with the combination of First Name and Last Name.

## Document Controller Hooks

The `before_save` method is just one of many hooks provided by the `Document` class. Here are some commonly used document hooks:

- `before_insert`: Called before a document is inserted into the database
- `after_insert`: Called after a document is inserted
- `validate`: Called before `before_save` and can be used for validations
- `before_save`: Called before a document is saved
- `after_save`: Called after a document is saved
- `before_submit`: Called before a document is submitted
- `after_submit`: Called after a document is submitted
- `before_cancel`: Called before a document is cancelled
- `after_cancel`: Called after a document is cancelled
- `on_trash`: Called before a document is deleted
- `after_delete`: Called after a document is deleted
- `before_update_after_submit`: Called before a submitted document is updated
- `after_update_after_submit`: Called after a submitted document is updated

These hooks allow you to write custom logic that executes at specific points during a document's lifecycle.

## Using Controller Methods Effectively

Controller methods are powerful tools for implementing business logic. Here are some common use cases:

1. **Field Computation**: Calculate field values based on other fields
2. **Validation**: Ensure data consistency and integrity
3. **Integration**: Interact with external systems
4. **Automation**: Trigger workflows or notifications

When implementing controller methods, remember:
- Keep your code modular and maintainable
- Handle exceptions appropriately
- Write clean, readable code with comments
- Don't modify standard fields unless necessary

## Next Steps

In the next tutorial, we'll learn about different types of DocTypes in Frappe, which will help us model more complex business scenarios for our Library Management System.