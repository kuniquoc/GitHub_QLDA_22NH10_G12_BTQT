# Extending the CLI

You can extend the Bench CLI by adding custom commands to your app.

---

## Steps to Extend the CLI

1. Create a `commands` folder in your app.
2. Add a Python file with your custom commands.
3. Use the `click` library to define commands.

### Example:
```python
import click

@click.command('hello')
def hello():
    click.echo('Hello, World!')
```

---

Was this article helpful? Let us know your feedback!