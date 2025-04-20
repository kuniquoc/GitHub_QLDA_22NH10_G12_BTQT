# Virtual DocType in Frappe Framework

Virtual DocTypes are DocTypes that don't have a corresponding database table. Instead, they fetch data from other sources, such as external APIs, other database tables, or computed data.

## Creating a Virtual DocType

A Virtual DocType is created by checking the "Is Virtual" option in the DocType form. When you create a Virtual DocType:

1. No database table is created for it
2. You need to implement methods to handle CRUD operations
3. Fields are defined like a regular DocType, but data storage is custom

## Implementation

To implement a Virtual DocType, you need to override several methods in the controller class:

```python
import frappe
from frappe.model.document import Document

class VirtualDocType(Document):
    # Get list of records (for List View)
    @staticmethod
    def get_list(args):
        # Return a list of dictionaries
        return [
            {"name": "RECORD-001", "title": "First Record", "status": "Active"},
            {"name": "RECORD-002", "title": "Second Record", "status": "Inactive"}
        ]
    
    # Load a single record
    def load_from_db(self):
        # Set document properties
        self.name = "RECORD-001"
        self.title = "First Record"
        self.status = "Active"
        self._original_modified = "2023-01-01 12:00:00"
        self.set_docstatus()  # Required
        self.run_method("after_read")  # Required
    
    # Refresh document from source
    def db_update(self):
        # Update external source
        pass
    
    # Insert new record
    def db_insert(self):
        # Insert to external source
        pass
    
    # Delete record
    def delete(self):
        # Delete from external source
        pass
```

## Use Cases

Virtual DocTypes are useful for:

1. **Integration with external systems**: Show data from external APIs
2. **Read-only views**: Create views on existing data without duplicating it
3. **Aggregated data**: Create documents that combine data from multiple tables
4. **Legacy system integration**: Interface with non-Frappe databases
5. **Dynamic content**: Generate documents on the fly based on calculations or rules

## Example: GitHub Issues as Virtual DocType

```python
import frappe
import requests
from frappe.model.document import Document

class GitHubIssue(Document):
    @staticmethod
    def get_list(args):
        repo = frappe.db.get_single_value("GitHub Settings", "repository")
        token = frappe.db.get_single_value("GitHub Settings", "access_token")
        
        headers = {"Authorization": f"token {token}"}
        response = requests.get(f"https://api.github.com/repos/{repo}/issues", headers=headers)
        
        issues = []
        for issue in response.json():
            issues.append({
                "name": str(issue["number"]),
                "title": issue["title"],
                "state": issue["state"],
                "created_by": issue["user"]["login"]
            })
        
        return issues
    
    def load_from_db(self):
        repo = frappe.db.get_single_value("GitHub Settings", "repository")
        token = frappe.db.get_single_value("GitHub Settings", "access_token")
        
        headers = {"Authorization": f"token {token}"}
        response = requests.get(f"https://api.github.com/repos/{repo}/issues/{self.name}", headers=headers)
        
        issue = response.json()
        self.title = issue["title"]
        self.state = issue["state"]
        self.body = issue["body"]
        self.created_by = issue["user"]["login"]
        self.created_at = issue["created_at"]
        self.labels = ", ".join([label["name"] for label in issue["labels"]])
        
        self._original_modified = self.created_at
        self.set_docstatus()
        self.run_method("after_read")
```

## Best Practices

1. Implement proper error handling for external data sources
2. Cache results when appropriate to improve performance
3. Handle authentication securely
4. Implement pagination for large datasets
5. Make sure to implement all required methods to ensure compatibility with UI components
6. Document clearly that the DocType is virtual to set expectations for users
7. Consider implementing search and filtering capabilities when possible