# OpenID Connect and Frappe Social Login

Frappe supports OpenID Connect, an essential standard for authenticating users. It also provides a setup for Frappe Social Login.

## OpenID Connect

To get an `id_token` along with an `access_token`, pass `openid` as the value for the scope parameter during the authorization request. The JSON response will include a JSON Web Token (`id_token`) signed with `HS256` and the Client Secret.

### Example Bearer Token with Scope `openid`

```json
{
  "token_type": "Bearer",
  "access_token": "ZJD04ldyyvjuAngjgBrgHwxcOig4vW",
  "scope": "openid",
  "expires_in": 3600,
  "refresh_token": "2pBTDTGhjzs2EWRkcNV1N67yw0nizS"
}
```

## Frappe Social Login Setup

### Primary Server

1. Go to `Setup > Integrations > Social Login Keys`.
2. Enter the Frappe Server URL (e.g., `https://frappe.io`).
3. Add OAuth Clients as required.

### Frappe App Server

1. Go to `Setup > Integrations > Social Login Keys`.
2. Add the Frappe Client ID and Client Secret.
3. Set the Frappe Server URL to the main server (e.g., `https://frappe.io`).

Now, users can log in using the Frappe icon on the login page.