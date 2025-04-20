# Users and Permissions

## Introduction to Users and Permissions

The Frappe Framework includes a comprehensive user management and permission system that controls who can access what data in your application. This system is designed to be:

1. **Role-based**: Permissions are assigned to roles, which are then assigned to users
2. **Granular**: Permissions can be set at the DocType level, field level, or even record level
3. **Flexible**: Custom permission rules can be implemented for complex business requirements
4. **Multi-tenant**: Each site has its own users and permission structure

This approach provides a robust security model that can be tailored to meet the needs of various organizational structures and data access requirements.

## Users

### User Types

Frappe supports different types of users:

1. **System Users**: Full access to Desk UI and backend functionality
2. **Website Users**: Access only to public-facing web pages and selected web forms
3. **Administrator**: Special user with unrestricted access

### User Management

Users can be managed through the UI or programmatically:

```python
# Create a new user
user = frappe.get_doc({
    "doctype": "User",
    "email": "jane.doe@example.com",
    "first_name": "Jane",
    "last_name": "Doe",
    "send_welcome_email": 1,
    "user_type": "System User",
    "roles": [
        {"role": "HR User"},
        {"role": "Employee"}
    ]
})
user.insert()
```

### User Profile

Each user has a profile with:

- Personal information (name, email, etc.)
- Security settings (password, two-factor authentication)
- Preferences (language, timezone, theme)
- Assigned roles

### Authentication

Frappe supports various authentication methods:

- Password-based authentication
- OAuth providers
- LDAP
- SAML
- Two-factor authentication (email, SMS, authenticator apps)

## Roles

### Role Concept

A role in Frappe is a grouping of permissions. Users are assigned one or more roles, and they inherit all permissions associated with those roles.

### Default Roles

Frappe comes with several built-in roles:

- **Administrator**: Complete access to the system
- **System Manager**: Manages users and permissions
- **HR Manager**: Human resources management
- **Accounts Manager**: Financial management
- **Sales Manager**: Sales and CRM
- **Purchase Manager**: Purchase and supply chain
- And many more

### Creating Custom Roles

You can create custom roles for specific business needs:

1. Using the UI: Go to "User > Role > New"
2. Programmatically:

```python
frappe.get_doc({
    "doctype": "Role",
    "role_name": "Quality Inspector",
    "desk_access": 1,
    "is_custom": 1
}).insert()
```

## Permission Model

### DocType Permissions

Permissions in Frappe are primarily set at the DocType level, controlling actions such as:

- **Read**: Ability to view records
- **Write**: Ability to create and modify records
- **Create**: Ability to create new records
- **Delete**: Ability to delete records
- **Submit**: Ability to submit documents
- **Cancel**: Ability to cancel submitted documents
- **Amend**: Ability to amend cancelled documents
- **Report**: Ability to access reports on the DocType
- **Import**: Ability to import data
- **Export**: Ability to export data
- **Print**: Ability to print records
- **Email**: Ability to email records
- **Share**: Ability to share records with other users

### Permission Rules

Permission rules link roles to DocTypes with specific permissions:

```
Role: HR Manager
DocType: Employee
Permissions: Read, Write, Create, Delete, Report, Import, Export
```

### User Permissions

User permissions restrict access to specific records based on field values:

```
User: jane.doe@example.com
DocType: Department
Value: "Engineering"
```

This would restrict Jane to only access records where the Department field is "Engineering".

## Implementing Permissions

### Setting DocType Permissions

DocType permissions can be set through:

1. **Permission Manager**: Access via "Settings > Permissions > Permission Manager"
2. **DocType Configuration**: When creating or editing a DocType
3. **JSON File**: Define permissions in custom applications

Example of permissions defined in a DocType JSON:

```json
{
  "permissions": [
    {
      "role": "HR Manager",
      "read": 1,
      "write": 1,
      "create": 1,
      "delete": 1,
      "report": 1
    },
    {
      "role": "Employee",
      "read": 1,
      "report": 1
    }
  ]
}
```

### Field-Level Permissions

You can restrict access to specific fields within a DocType:

1. **Perm Level**: Assign permission levels to fields (0, 1, 2, etc.)
2. **Role Permissions**: Define which roles can access which perm levels

Example field definition with perm_level:

```json
{
  "fieldname": "salary",
  "fieldtype": "Currency",
  "label": "Salary",
  "perm_level": 1
}
```

Then in permissions, specify which roles have access to perm_level 1:

```json
{
  "role": "HR Manager",
  "permlevel": 1,
  "read": 1,
  "write": 1
}
```

### Document-Level Permissions

Document-level permissions restrict access to specific records and can be implemented through:

1. **User Permissions**: Restrict access based on field values
2. **Custom Scripts**: Implement complex permission logic using scripts
3. **Permission Queries**: Define custom SQL queries for permission checks

### Permission Customization

For complex permission requirements, you can:

1. **Override Permission Controller**: Create a custom permission controller
2. **Use has_permission Hook**: Implement custom permission logic

Example of a custom has_permission hook:

```python
def has_permission(doc, ptype, user):
    # Custom permission logic
    if ptype == "read" and doc.is_public:
        return True
    
    # For managers, allow full access to their department's records
    department = frappe.get_value("Employee", {"user_id": user}, "department")
    if department and doc.department == department:
        return True
    
    # Fall back to standard permissions
    return False

# Register the hook
permissions = {
    "Project": {
        "has_permission": has_permission
    }
}
```

## Common Permission Patterns

### Role-Based Access Control

The basic pattern where users are assigned roles, and roles are granted permissions:

1. Create roles for different job functions
2. Assign appropriate permissions to each role
3. Assign roles to users

### Organizational Hierarchy

For organizations with hierarchical structures:

1. Use User Permissions to restrict data by department, company, etc.
2. Implement custom permission queries for manager-subordinate relationships

### Multi-Company Setup

For multi-company environments:

1. Use the Company field as a permission filter
2. Set User Permissions to restrict users to specific companies
3. Create company-specific roles if needed

### Project-Based Access

For project-based organizations:

1. Implement Project DocType with team members
2. Define custom permission rules based on project membership
3. Use has_permission hook for project-specific logic

## Best Practices

1. **Follow the Principle of Least Privilege**: Grant only the permissions necessary for users to perform their tasks.
2. **Use Roles Effectively**: Create roles based on job functions, not individuals.
3. **Leverage User Permissions**: Use User Permissions for record-level access control.
4. **Document Your Permission Structure**: Keep documentation of your permission setup for easier maintenance.
5. **Regular Audits**: Periodically review user permissions to ensure they remain appropriate.
6. **Test Permission Changes**: Always test permission changes thoroughly before deploying to production.
7. **Use Role Profiles**: Group commonly used roles into Role Profiles for easier user setup.
8. **Avoid Custom Permission Logic** when standard features can achieve the same result.

## Troubleshooting Permissions

### Common Issues

1. **User cannot access a document**: Check if the user has appropriate role, and that the role has read permission for the DocType.
2. **User cannot edit a document**: Verify write permission is granted to the user's role.
3. **User can see records they shouldn't**: Check for conflicts in User Permissions or custom permission rules.

### Debugging Tools

1. **has_permission method**: Use frappe.has_permission() to check permissions programmatically.
2. **get_roles method**: Use frappe.get_roles() to check a user's assigned roles.
3. **Permission Query Report**: Check the report "User Permissions" to see all permissions for a user.

### Permission Troubleshooting Steps

1. Verify the user's assigned roles
2. Check DocType permissions for those roles
3. Look for applicable User Permissions
4. Check for custom permission hooks or scripts
5. Review field-level permissions
6. Check for ownership restrictions

## Conclusion

The Frappe Framework's user and permission system provides a flexible, powerful way to control data access in your applications. By leveraging roles, DocType permissions, user permissions, and custom logic where needed, you can implement sophisticated access control that meets complex business requirements while maintaining security and data privacy.