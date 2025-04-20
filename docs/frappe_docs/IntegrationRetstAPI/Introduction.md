# Introduction to Frappe REST API

Frappe ships with an HTTP API that can be classified into:

- **Remote Procedure Calls (RPC)**: To call whitelisted methods.
- **Representational State Transfer (REST)**: To manipulate resources.

The base URL for the API is:

```
https://{your frappe instance}
```

For example, if your instance is `demo.erpnext.com`, the endpoint:

```
GET /api/resource/User
```

translates to:

```
GET https://demo.erpnext.com/api/resource/User
```

---

## API v1

All v1 API endpoints are prefixed with `/api/`. Starting from Frappe Framework version 15, they can also be prefixed with `/api/v1/`.

### RPC

A request to an endpoint like:

```
/api/method/dotted.path.to.method
```

will call a whitelisted Python method. For example:

```
GET /api/method/frappe.auth.get_logged_user
```

calls the following function from Frappe's auth module:

```python
@frappe.whitelist()
def get_logged_user():
    return frappe.session.user
```

**Response:**

```json
{
    "message": "Administrator"
}
```

### REST

All documents in Frappe are available via a RESTful API with the prefix `/api/resource/`. You can perform all CRUD operations:

- **Create**: Send a `POST` request to `/api/resource/{doctype}`.
- **Read**: Get a document by its name using `/api/resource/{doctype}/{name}`.
- **Update**: Send a `PUT` request to `/api/resource/{doctype}/{name}`. This acts like a `PATCH` request where you only send the parts you want to change.
- **Delete**: Send a `DELETE` request to `/api/resource/{doctype}/{name}`.

---

## API v2

API v2 is available starting from Frappe Framework v15. All v2 API endpoints are prefixed with `/api/v2/`.

### RPC v2

RPC endpoints are available at the `/api/v2/method/` prefix. Examples include:

- `/api/v2/method/login`: Handle user login.
- `/api/v2/method/logout`: Log out the current user.
- `/api/v2/method/ping`: Check server status.
- `/api/v2/method/upload_file`: Upload a file.
- `/api/v2/method/dotted.path.to.method`: Call any whitelisted method.
- `/api/v2/method/<doctype>/<method>`: Call a whitelisted method from a Doctype controller.
- `/api/v2/method/run_doc_method`: Run a whitelisted method on a document.

### REST v2

API v2 provides a more RESTful interface with the prefixes `/api/v2/document/` and `/api/v2/doctype/`. Supported operations include:

#### Document Operations

- **Create**: Send a `POST` request to `/api/v2/document/{doctype}`.
- **Read**: Send a `GET` request to `/api/v2/document/{doctype}/{name}/`.
- **Update**: Send a `PATCH` or `PUT` request to `/api/v2/document/{doctype}/{name}/`.
- **Delete**: Send a `DELETE` request to `/api/v2/document/{doctype}/{name}/`.
- **Get a clean copy**: Send a `GET` request to `/api/v2/document/{doctype}/{name}/copy`.
- **Execute Method**: Send a `GET` or `POST` request to `/api/v2/document/{doctype}/{name}/method/{method}`.

  Common values for `method` include:

  - `add_comment?text=hello`
  - `submit`
  - `cancel`
  - `rename?name=newname`

#### DocType Operations

- **Get Metadata**: Send a `GET` request to `/api/v2/doctype/{doctype}/meta`.
- **Get Count**: Send a `GET` request to `/api/v2/doctype/{doctype}/count`.
- **List Documents**: Send a `GET` request to `/api/v2/document/{doctype}`. Supports pagination and field selection through query parameters.