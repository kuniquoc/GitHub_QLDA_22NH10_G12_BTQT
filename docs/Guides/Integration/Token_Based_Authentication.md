# Token Based Authentication

Token-based authentication is a security technique that authenticates users attempting to access a server. It is available starting with Frappe version 11.0.3.

## How It Works

- A combination of API Key and API Secret forms a token used to authenticate requests.
- Tokens can be used for full CRUD operations.

## Generating a Token

1. **Web Interface**: Go to `User > API Access > Generate Keys`.
2. **Command Line**:

```bash
bench execute frappe.core.doctype.user.user --args ['user_name']
```

3. **RPC**:

```http
/api/method/frappe.core.doctype.user.user?user="user_name"
```

## Notes

- API keys cannot be regenerated.
- Only users with the System Manager role can generate keys.