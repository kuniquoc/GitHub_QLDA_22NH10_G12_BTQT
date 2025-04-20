# Manipulating Documents

Frappe provides REST API endpoints to manipulate documents. These endpoints allow you to perform CRUD (Create, Read, Update, Delete) operations on documents.

---

## 1. Retrieve a Specific Document

### Endpoint:
```
GET /api/resource/{DocType}/{DocumentName}
```

### Parameters:
- **DocType** (string): The type of the document you'd like to retrieve (e.g., `Customer`).
- **DocumentName** (string): The unique ID of the document (e.g., `CUST-00001`).

### Example:
Retrieve a Customer with the name (ID) `CUST-00001`:
```bash
curl -X GET https://{your frappe instance}/api/resource/Customer/CUST-00001
```

---

## 2. Create a New Document

### Endpoint:
```
POST /api/resource/{DocType}
```

### Parameters:
- **DocType** (string): The type of document you'd like to create (e.g., `Customer`).

### Headers:
- `Content-Type: application/json`

### Request Body:
```json
{
  "fieldname": "value"
}
```

### Example:
Create a new Lead named `Mustermann`:
```bash
curl -X POST https://{your frappe instance}/api/resource/Lead \
 -H 'Content-Type: application/json' \
 -H 'Accept: application/json' \
 -d '{"lead_name":"Mustermann"}'
```

---

## 3. Update a Specific Document

### Endpoint:
```
PUT /api/resource/{DocType}/{DocumentName}
```

### Parameters:
- **DocType** (string): The type of the document you'd like to update (e.g., `Customer`).
- **DocumentName** (string): The unique ID of the document (e.g., `EMP-00001`).

### Headers:
- `Content-Type: application/json`

### Request Body:
```json
{
  "fieldname": "value"
}
```

### Example:
Update the `contact_date` of a Lead with the name `LEAD-00001`:
```bash
curl -X PUT https://{your frappe instance}/api/resource/Lead/LEAD-00001 \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{"contact_date":"2018-10-08"}'
```

### Response:
```json
{
  "data": {
    "doctype": "Lead",
    "name": "LEAD-00001",
    "contact_date": "2018-10-08",
    "...": "..."
  }
}
```

---

## 4. Delete a Specific Document

### Endpoint:
```
DELETE /api/resource/{DocType}/{DocumentName}
```

### Parameters:
- **DocType** (string): The type of the document you'd like to delete (e.g., `Customer`).
- **DocumentName** (string): The unique ID of the document (e.g., `EMP-00001`).

### Example:
Delete a Customer with the name `CUST-00001`:
```bash
curl -X DELETE https://{your frappe instance}/api/resource/Customer/CUST-00001
```

---

## 5. List Documents

### Endpoint:
```
GET /api/resource/{DocType}
```

### Parameters:
- **DocType** (string): The type of document you'd like to list (e.g., `Customer`).
- **fields** (array): Specify the fields to include in the response (default: `["name"]`).
- **filters** (array): Apply SQL-like conditions to filter the results.
- **limit_page_length** (int): Number of items per page (default: 20).
- **limit_start** (int): Offset for pagination.

### Example:
Get at most 20 names (IDs) of all Customers whose phone number is `4915227058038`:
```bash
curl -X GET https://{your frappe instance}/api/resource/Customer?fields=["name"] \
 &filters=[["Customer","phone","=","4915227058038"]]
```

---

## Notes

- **Authentication**: Ensure you include the appropriate authentication headers (e.g., Basic Authentication or OAuth2).
- **Content-Type**: Use `application/json` for requests that include a body.
- **Authorization**: Include the `Authorization` header for secure access.

---

Author: Raffael Meyer (raffael@alyf.de)