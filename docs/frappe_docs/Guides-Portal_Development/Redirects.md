# Redirects

You can add redirects by using the `website_redirects` hook. The optional field `redirect_http_status` allows you to specify a custom HTTP status code for the redirect. If not specified, the default is 301.

## Examples

```python
website_redirects = [
    # Absolute location
    {"source": "/from", "target": "https://mysite/from"},

    # Relative location
    {"source": "/from", "target": "/main", "redirect_http_status": 307},

    # Use regex
    {"source": "/from/(.*)", "target": "/main/\1"}
]
```