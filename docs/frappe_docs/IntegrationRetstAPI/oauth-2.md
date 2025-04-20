# OAuth 2 Integration in Frappe

Frappe supports OAuth 2 for secure authentication and authorization. This guide explains how to use OAuth 2 endpoints for token-based authentication.

---

## Authorization Request

To initiate the OAuth 2 flow, use the following endpoint:

### Endpoint: `GET /api/method/frappe.integrations.oauth2.authorize`

#### Parameters (in query):
- `client_id` (string): ID of your OAuth2 application.
- `state` (string): Arbitrary value used to maintain state between the request and callback. Helps prevent cross-site request forgery.
- `response_type` (string): Must be `code`.
- `scope` (string): The scope of access that should be granted to your application.
- `redirect_uri` (string): Callback URI that the user will be redirected to after authorization.
- `code_challenge_method` (string) (OPTIONAL): Can be `s256` or `plain`.
- `code_challenge` (string) (OPTIONAL): Used for PKCE (Proof Key for Code Exchange).

#### Example:
```bash
curl -X GET https://{your frappe instance}/api/method/frappe.integrations.oauth2.authorize \
 --data-urlencode 'client_id=511cb2ac2d' \
 --data-urlencode 'state=444' \
 --data-urlencode 'response_type=code' \
 --data-urlencode 'scope=openid all' \
 --data-urlencode 'redirect_uri=https://app.getpostman.com/oauth2/callback'
```

If the user clicks "Allow," the redirect URI will be called with an authorization code in the query parameters:
```
https://{redirect uri}?code=plkj2mqDLwaLJAgDBAkyR1W8Co08Ud&state=444
```

If the user clicks "Deny," you will receive an error:
```
https://{redirect uri}?error=access_denied
```

---

## Token Exchange for Authorization Code Grant

Trade the authorization code for an access token using the following endpoint:

### Endpoint: `POST /api/method/frappe.integrations.oauth2.get_token`

#### Headers:
- `Content-Type: application/x-www-form-urlencoded`

#### Parameters (in body):
- `grant_type` (string): Must be `authorization_code`.
- `code` (string): Authorization code received in the redirect URI.
- `client_id` (string): ID of your OAuth2 application.
- `redirect_uri` (string): Registered redirect URI of the client app.
- `code_verifier` (string): Used during the Authorization Request with `code_challenge_method` and `code_challenge`.

#### Example:
```bash
curl -X POST https://{your frappe instance}/api/method/frappe.integrations.oauth2.get_token \
 -H 'Content-Type: application/x-www-form-urlencoded' \
 -H 'Accept: application/json' \
 -d 'grant_type=authorization_code&code=wa1YuQMff2ZXEAu2ZBHLpJRQXcGZdr&redirect_uri=https%3A%2F%2Fapp.getpostman.com%2Foauth2%2Fcallback&client_id=af615c2d3a&code_verifier=420'
```

#### Response:
```json
{
  "access_token": "pNO2DpTMHTcFHYUXwzs74k6idQBmnI",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "cp74cxbbDgaxFuUZ8Usc7egYlhKbH1",
  "scope": "openid all",
  "id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## OpenID User Info Endpoint

Retrieve user information using the following endpoint:

### Endpoint: `GET /api/method/frappe.integrations.oauth2.openid_profile`

#### Headers:
- `Authorization: Bearer <valid_access_token>`

#### Example:
```bash
curl -X GET https://{your frappe instance}/api/method/frappe.integrations.oauth2.openid_profile \
 -H 'Authorization: Bearer pNO2DpTMHTcFHYUXwzs74k6idQBmnI'
```

#### Response:
```json
{
  "sub": "1234567890",
  "name": "J. Doe",
  "given_name": "J",
  "family_name": "Doe",
  "email": "j@doe.com",
  "roles": ["System Manager", "Sales Manager"]
}
```

---

## Revoke Token Endpoint

Revoke an access token or refresh token using the following endpoint:

### Endpoint: `POST /api/method/frappe.integrations.oauth2.revoke_token`

#### Headers:
- `Content-Type: application/x-www-form-urlencoded`

#### Parameters:
- `token` (string): Access token or refresh token to be revoked.

#### Example:
```bash
curl -X POST https://{your frappe instance}/api/method/frappe.integrations.oauth2.revoke_token \
 -H 'Content-Type: application/x-www-form-urlencoded' \
 -H 'Accept: application/json' \
 -d 'token=pNO2DpTMHTcFHYUXwzs74k6idQBmnI'
```

#### Response:
Always returns an empty response with HTTP status code `200`:
```json
{}
```

---

## Introspect Token Endpoint

Check the validity of a token using the following endpoint:

### Endpoint: `POST /api/method/frappe.integrations.oauth2.introspect_token`

#### Headers:
- `Content-Type: application/x-www-form-urlencoded`

#### Parameters:
- `token_type_hint` (string): `access_token` or `refresh_token` (defaults to `access_token`).
- `token` (string): Token to be introspected.

#### Example:
```bash
curl -X POST https://{your frappe instance}/api/method/frappe.integrations.oauth2.introspect_token \
 -H 'Content-Type: application/x-www-form-urlencoded' \
 -H 'Accept: application/json' \
 -d 'token=pNO2DpTMHTcFHYUXwzs74k6idQBmnI'
```

#### Response:
```json
{
  "client_id": "511cb2ac2d",
  "trusted_client": 1,
  "active": true,
  "exp": 1619523326,
  "scope": "openid all"
}
```

---

## Notes

- OAuth 2 is a secure and widely used protocol for authentication and authorization.
- Use the `Authorization` header with the appropriate token type (`Bearer`) for authenticated requests.
- Always revoke tokens when they are no longer needed.

For more details, refer to the [OAuth 2 Specification](https://oauth.net/2/).