# Simple Authentication

Frappe provides simple authentication methods for interacting with its REST API. Below are the details of the available endpoints and their usage.

---

## POST /api/method/login

This endpoint is used to log in a user.

### Request

- **Method**: `POST`
- **URL**: `/api/method/login`
- **Content-Type**: `application/x-www-form-urlencoded`

### Parameters (in body)

- `usr` (string): Username
- `pwd` (string): Password

### Example

```bash
curl -X POST https://{your frappe instance}/api/method/login \
 -H 'Content-Type: application/json' \
 -H 'Accept: application/json' \
 -d '{"usr":"Administrator","pwd":"admin"}'
```

### Response

- **HTTP Code**: `200`
- **Content-Type**: `application/json`

```json
{
  "home_page": "/desk",
  "full_name": "Administrator",
  "message": "Logged in"
}
```

- **Cookie**: `sid` (send this to authenticate future requests).
- **Expires**: In three days.

---

## GET /api/method/logout

This endpoint is used to log out the currently authenticated user.

### Request

- **Method**: `GET`
- **URL**: `/api/method/logout`

### Example

```bash
curl -X GET https://{your frappe instance}/api/method/logout
```

### Response

- **HTTP Code**: `200`
- **Content-Type**: `application/json`

```json
{}
```

---

## GET /api/method/frappe.auth.get_logged_user

This endpoint retrieves the ID of the currently authenticated user.

### Request

- **Method**: `GET`
- **URL**: `/api/method/frappe.auth.get_logged_user`

### Example

```bash
curl -X GET https://{your frappe instance}/api/method/frappe.auth.get_logged_user
```

### Response

- **HTTP Code**: `200`
- **Content-Type**: `application/json`

```json
{
  "message": "Administrator"
}
```

---

## Error Handling

If the username or password is incorrect, the API will return the following error:

- **HTTP Code**: `401`
- **Content-Type**: `text/html`

```html
Wrong password or username.
```

---

### Notes

- Always include the `sid` cookie in subsequent requests after logging in.
- The session expires in three days unless explicitly logged out.

---

Author: Raffael Meyer (raffael@alyf.de)