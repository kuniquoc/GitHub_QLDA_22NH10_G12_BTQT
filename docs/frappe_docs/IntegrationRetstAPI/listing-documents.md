# Listing Documents

To list documents in Frappe, you can make a `GET` request to the following endpoint:

```
/api/resource/{doctype}
```

---

## Example Request

### Endpoint:
```
GET /api/resource/Person
```

### Default Behavior:
- All listings are returned paginated by **20 items**.
- The response is returned as a JSON object, and the listing is an array with the key `data`.

### Example Response:
```json
{
  "data": [
    {
      "name": "000000012"
    },
    {
      "name": "000000008"
    }
  ]
}
```

---

## Customizing the Response

### 1. Changing Page Size
To change the page size, use the query parameter `limit_page_length`.

### 2. Requesting Successive Pages
To request successive pages, use the query parameter `limit_start`.

---

### 3. Adding More Fields
By default, only the `name` field is included in the listing. To include additional fields, pass the `fields` parameter as a JSON array containing the field names.

#### Example Request:
```
GET /api/resource/Person/?fields=["name","first_name"]
```

#### Example Response:
```json
{
  "data": [
    {
      "name": "000000012",
      "first_name": "Jane"
    },
    {
      "name": "000000008",
      "first_name": "John"
    }
  ]
}
```

---

### 4. Filtering the Listing
You can filter the listing using SQL-like conditions by passing the query parameter `filters`. The `filters` parameter must be a JSON array containing one or multiple conditions. Each condition is an array in the format:

```
[{doctype}, {field}, {operator}, {operand}]
```

#### Example:
To get the `name` (ID) of all persons with the first name "Jane":

```
GET /api/resource/Person?filters=[["Person","first_name","=","Jane"]]
```

#### Example Response:
```json
{
  "data": [
    {
      "name": "000000012"
    }
  ]
}
```

---

### Authors:
- Rushabh Mehta (rushabh@erpnext.com)
- Raffael Meyer (raffael@alyf.de)