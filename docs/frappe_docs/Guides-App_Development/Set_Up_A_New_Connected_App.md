# Set up a New Connected App

You can use a Connected App to allow your Frappe instance to access other web services on your behalf. This example shows how to connect to Google Mail, but you can use any service supporting OAuth 2.0.

## Steps

1. Create a new Connected App and give it a name.
2. Enter the URL for OpenID Configuration (e.g., `/.well-known/openid-configuration`) and click on "Get OpenID Configuration".
3. If you don't know this URL, manually enter the Authorization URI and Token URI. These can be found in the documentation of the specific integration or third-party service.
4. Save the configuration. A new read-only field called Redirect URI will appear. Register this Redirect URI with your provider (e.g., Google).
5. Define extra parameters if required (e.g., `access_type=offline` for background access).

## Example

For Google Mail:
- Use the scope `https://mail.google.com/`.
- Ensure authorized JavaScript origins and redirect URIs are correct.

Once configured, users can click on "Connect to ..." to open the third-party service's consent screen. After consent, the server exchanges a code for an access token and optionally a refresh token.