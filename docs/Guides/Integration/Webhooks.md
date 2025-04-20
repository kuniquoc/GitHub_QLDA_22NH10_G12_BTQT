# Webhooks

Webhooks are "user-defined HTTP callbacks" that trigger on specific document events under certain conditions. When the `doc_event` occurs, the source site makes an HTTP request to the configured URI.

## Configuring a Webhook

1. Go to `Integrations > Webhook > Webhook`.
2. Select the DocType for which the Webhook needs to be triggered (e.g., `Quotation`).
3. Select the Doc Event that will trigger the Webhook (e.g., `on_update`).
4. Optionally, set additional document conditions.
5. Enter a valid request URL.
6. Select the Request Method (e.g., `POST`).
7. Optionally, add HTTP headers (e.g., for sending an API key).

## Example JSON Request Body

For a Webhook on a sales transaction:

```json
{
  "id": "{{ doc.name }}",
  "total": "{{ doc.total }} EUR",
  "customer": "{{ doc.customer }}",
  "created": "{{ doc.creation }}",
  "items": {{ doc["items"] | tojson }}
}
```