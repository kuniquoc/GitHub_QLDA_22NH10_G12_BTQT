# Types of DocType

## Introduction

In this tutorial, we'll learn about the different types of DocTypes in Frappe Framework by creating more DocTypes for our Library Management application. We'll explore concepts like linked DocTypes, submittable DocTypes, and single DocTypes.

## Library Membership DocType

Let's create another DocType called **Library Membership** with the following fields:

1. **Library Member** (Field Type: Link, Options: Library Member, Mandatory: Yes)
2. **Full Name** (Field Type: Data, Read Only: Yes, Fetch From: `library_member.full_name`)
3. **From Date** (Field Type: Date)
4. **To Date** (Field Type: Date)
5. **Paid** (Field Type: Check)

For this DocType, we'll enable special features:
- Enable **Is Submittable** in the DocType settings
- Set Naming as `LMS.#####` (an auto-incremented series with prefix)
- Restrict permissions to the **Librarian** role
- Set the Title Field to `full_name` in View Settings

After creating the DocType, create a new Library Membership record to see how the Link field works.

### Link Fields and Fetching Values

The **Library Member** field is a Link field, which is similar to a Foreign Key in other database systems. It allows you to link to a record in another DocType.

When you select a Library Member, notice that the Full Name field is automatically populated. This is because we set up field fetching with `Fetch From: library_member.full_name`. This powerful feature allows you to pull data from linked DocTypes.

## Linked DocTypes

All DocTypes in Frappe can be linked to other DocTypes using Link fields. We can broadly classify DocTypes into:

1. **Master DocTypes** - Store entity data (e.g., Article, Library Member)
2. **Transactional DocTypes** - Store transaction data (e.g., Library Membership)

## Submittable DocTypes

When you enable **Is Submittable** for a DocType, it gains three possible states:
- **Draft**: Can be modified freely
- **Submitted**: Cannot be modified
- **Cancelled**: Document is invalidated

Submittable DocTypes include an additional field called **Amended From** to track document amendments. Once a document is cancelled, it can be amended (duplicated), and the new document will be linked to the cancelled one via this field.

### Validation for Library Membership

Let's add validation to ensure that a member cannot have overlapping memberships. Edit the `library_membership.py` file:

```python
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")
        
        # get loan period and compute to_date by adding loan_period to from_date
        loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
```

This controller method runs before the document is submitted. It:
1. Checks if there's already an active membership for the member
2. Automatically calculates the `to_date` based on the loan period in Library Settings

## Library Transaction DocType

Next, let's create a DocType to record the issue and return of articles. Create a DocType called **Library Transaction** with the following fields:

1. **Article** (Field Type: Link, Options: Article)
2. **Library Member** (Field Type: Link, Options: Library Member)
3. **Type** (Field Type: Select, Options: Issue\nReturn)
4. **Date** (Field Type: Date)

Also enable **Is Submittable** for this DocType.

### Validation for Library Transaction

Let's add validation to check if:
1. The library member has an active membership
2. The article is available when being issued
3. The article is issued when being returned
4. The maximum limit of issued articles hasn't been reached

Edit the `library_transaction.py` file:

```python
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            self.validate_maximum_limit()
            # set the article status to be Issued
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        elif self.type == "Return":
            self.validate_return()
            # set the article status to be Available
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # article cannot be issued if it is already issued
        if article.status == "Issued":
            frappe.throw("Article is already issued by another member")

    def validate_return(self):
        article = frappe.get_doc("Article", self.article)
        # article cannot be returned if it is not issued first
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")

    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
        count = frappe.db.count(
            "Library Transaction",
            {
                "library_member": self.library_member,
                "type": "Issue",
                "docstatus": DocStatus.submitted(),
            },
        )
        if count >= max_articles:
            frappe.throw("Maximum limit reached for issuing articles")

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")
```

## Single DocType

Finally, let's create a DocType to store global settings for our Library. Create a DocType called **Library Settings** with the following fields:

1. **Loan Period** (Field Type: Int, Description: Number of days)
2. **Maximum Number of Issued Articles** (Field Type: Int)

Enable **Is Single** for this DocType.

### Single DocTypes

When you enable **Is Single** for a DocType, it becomes a singleton with only one record. Instead of creating a separate database table, all values for single DocTypes are stored in a table called `tabSingles`. This is useful for storing global settings.

After creating the Library Settings DocType, click on **Go to Library Settings** to set values for the Loan Period and Maximum Number of Issued Articles.

## Testing the Full System

Now that we have created all the necessary DocTypes and their controllers, let's test our Library Management system:

1. Create a few Articles
2. Create a Library Member
3. Create a Library Membership for the member
4. Submit the membership
5. Create a Library Transaction to issue an article to the member
6. Submit the transaction
7. Try to issue more articles than the maximum limit
8. Create a transaction to return the article
9. Submit the transaction

Each step should validate according to the business logic we've defined in our controller methods.

## Summary

In this tutorial, we learned about different types of DocTypes in Frappe Framework:

1. **Linked DocTypes** - DocTypes that are linked to other DocTypes using Link fields
2. **Submittable DocTypes** - DocTypes with document states (Draft, Submitted, Cancelled)
3. **Single DocTypes** - DocTypes that store singleton data, like global settings

We also implemented complex business logic using controller methods, including validations for:
- Preventing overlapping memberships
- Ensuring members have active memberships before issuing articles
- Validating article availability
- Enforcing maximum limits for issued articles

These concepts and patterns will help you model and implement complex business scenarios in your own Frappe applications.

## Next Steps

In the next tutorial, we'll learn about Form Scripts, which allow us to add client-side interactivity to our DocType forms.