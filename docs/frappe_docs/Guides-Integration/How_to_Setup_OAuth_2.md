# How to Setup OAuth 2

OAuth 2.0 is built into Frappe, allowing third-party apps to access user resources based on Frappe's Role and User permission system.

## OAuth 2 Roles

1. **Resource Owner**: Grants access to a protected resource.
2. **Resource Server**: Hosts the protected resources.
3. **Client**: Makes protected resource requests on behalf of the resource owner.
4. **Authorization Server**: Issues access tokens to the client after authenticating the resource owner.

## Setup OAuth 2 Provider

1. Go to `Setup > Integrations > OAuth Provider Settings`.
2. Configure the confirmation message behavior as "Force" or "Auto".

## Add a Client App

1. Go to `Setup > Integrations > OAuth Client`.
2. Fill in the following details:
   - **App Name**: Enter the app name (e.g., CAVS).
   - **Skip Authorization**: Check if no confirmation message is needed.
   - **Scopes**: List of scopes separated by space.
   - **Redirect URIs**: List of URIs separated by space.
   - **Grant Type**: Select `Authorization Code` or `Implicit`.
   - **Response Type**: Select `Code` or `Token` based on the grant type.