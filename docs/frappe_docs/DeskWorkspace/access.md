# Access

Workspaces in Frappe can be restricted based on **Modules** and **Roles**. Below are the details on how access can be managed:

---

## Modules

Users can have access to different modules, and standard workspaces are visible based on access to those modules.

### Example:
- If a user loses access to a specific module (e.g., Website Module), they will no longer see the corresponding workspace (e.g., Website Workspace).

---

## Roles

Even if users have access to a module, you can restrict access to its standard workspace based on roles.

### Example:
- Jack Doe, a manager with the **Workspace Manager Role**, configures the Website Workspace to be visible only to users with the **Website Manager Role**.
- Jane Doe, who has access to the Website Module but does not have the Website Manager Role, will not see the Website Workspace.
- John Doe, who has both Website Module access and the Website Manager Role, will see the Website Workspace.

---

## Default Workspace

The default workspace shown when a user logs in can be configured for each user. By default:
- The user will see the workspace they were last in.
- Alternatively, the default workspace can be set using the **Default Workspace** field in the User settings form, accessible via the **My Settings** option in the avatar menu.

---

Was this article helpful? Let us know your feedback!