# Token Based Authentication

Available starting with **v11.0.3**, Frappe supports token-based authentication for API requests. The HTTP `Authorization` request header contains the credentials to authenticate a user with a server. It consists of the authorization type (`token` or `Basic`) and the corresponding token.

```
Authorization: <type> <token>
```

The token consists of `api-key` and `api-secret` joined by a colon.

---

## Generating API Key and API Secret

To generate the API Key and API Secret:

1. Go to the **User list** and open a user.
2. Click on the **Settings** tab. (Skip this step if you don't see tabs.)
3. Expand the **API Access** section and click on **Generate Keys**.
4. You will see the generated **API Key** and **API Secret** in this section.

---

## Using the Token for Authentication

### Token Authentication

The `Authorization` header for token-based authentication looks like this:

```
Authorization: token <api_key>:<api_secret>
```

**Example in Python:**

```python
import requests

url = "http://frappe.local:8000/api/method/frappe.auth.get_logged_user"
headers = {
    'Authorization': "token <api_key>:<api_secret>"
}
response = requests.request("GET", url, headers=headers)
```

---

### Basic Authentication

If the `Basic` authentication scheme is used, the credentials are a combination of `api_key` and `api_secret` and are constructed as follows:

1. Combine the values with a colon: `<api_key>:<api_secret>`.
2. Base64 encode the resulting string: `base64encode(<api_key>:<api_secret>)`.

The `Authorization` header for basic authentication looks like this:

```
Authorization: Basic base64encode("<api_key>:<api_secret>")
```

**Example in Python:**

```python
import requests
import base64

url = "http://frappe.local:8000/api/method/frappe.auth.get_logged_user"
headers = {
    'Authorization': "Basic %s" % base64.b64encode(b"<api_key>:<api_secret>").decode("utf-8")
}
response = requests.request("GET", url, headers=headers)
```

---

### OAuth 2 Access Token

If the OAuth 2 Access Token is used to authenticate requests, the token is an opaque `access_token` string provided by the Frappe server after setting up OAuth 2 and generating the token.

The `Authorization` header for OAuth 2 looks like this:

```
Authorization: Bearer <access_token>
```

**Example in Python:**

```python
import requests

url = "http://frappe.local:8000/api/method/frappe.auth.get_logged_user"
headers = {
    "Authorization": "Bearer %s" % access_token
}
response = requests.request("GET", url, headers=headers)
```

---

## Notes

- Using the generated API Key and API Secret, you can authenticate your API requests. Every request made with these keys will be logged against the user you selected during the setup.
- Roles and permissions will be checked against the user associated with the API Key and API Secret.
- You can create a dedicated user specifically for API calls to better manage access and logs.

---

## Further Resources

- [Authorization Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)