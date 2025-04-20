# Asset Bundling

## Introduction to Asset Bundling

Asset bundling is the process of combining multiple JavaScript and CSS files into a smaller number of optimized files to improve website loading performance. The Frappe Framework includes a robust asset bundling system that helps:

1. **Reduce HTTP Requests**: By combining multiple files into one
2. **Minify Code**: Removing unnecessary characters to reduce file size
3. **Organize Dependencies**: Ensuring files load in the correct order
4. **Cache Management**: Efficient browser caching through versioning

## Asset Structure

In Frappe applications, assets like JavaScript and CSS files are organized within the app's directory structure:

```
my_app/
└── my_app/
    ├── public/
    │   ├── js/
    │   │   └── my_script.js
    │   ├── css/
    │   │   └── my_style.css
    │   └── scss/
    │       └── my_style.scss
    └── ...
```

When Frappe builds these assets, they are processed and moved to a centralized location in the `sites/assets` directory.

## Asset Bundling Process

### Build Process

Frappe uses a build system that:

1. Looks for assets in all installed apps
2. Processes them (compiles SCSS to CSS, transpiles ES6+ to ES5, etc.)
3. Bundles them according to configuration
4. Minifies the bundles
5. Adds version hashes for cache-busting

### Build Tools

Frappe uses several tools for asset processing:

- **Rollup**: For JavaScript bundling
- **Babel**: For JavaScript transpilation
- **Terser**: For JavaScript minification
- **SASS**: For SCSS compilation
- **PostCSS**: For CSS processing and optimization

## Including Assets in Your App

### JavaScript Files

To include JavaScript files in your app, you can:

1. Add them to the `public/js` directory
2. Specify them in the `hooks.py` file:

```python
# In hooks.py
app_include_js = ["/assets/my_app/js/my_script.js"]
```

### CSS Files

Similarly, for CSS files:

```python
# In hooks.py
app_include_css = ["/assets/my_app/css/my_style.css"]
```

### SCSS Files

SCSS files will be automatically compiled to CSS. You can organize your SCSS files in the `public/scss` directory.

## Bundling Configuration

### Bundle Types

Frappe supports several types of bundles:

1. **App-level bundles**: Basic JS and CSS for each app
2. **Page-specific bundles**: Assets loaded only on specific pages
3. **Website bundles**: For the public-facing website
4. **Desk bundles**: For the admin interface (Desk)

### Configuring Bundles

Bundles are configured through the `hooks.py` file in each app:

```python
# Standard bundles for all pages
app_include_js = ["/assets/js/my_app.min.js"]
app_include_css = ["/assets/css/my_app.min.css"]

# Desk (admin interface) bundles
desk_include_js = ["/assets/js/my_desk_extension.min.js"]
desk_include_css = ["/assets/css/my_desk_extension.min.css"]

# Website-only bundles
website_include_js = ["/assets/js/my_website.min.js"]
website_include_css = ["/assets/css/my_website.min.css"]

# DocType-specific assets
doctype_js = {
    "Customer": "public/js/customer.js"
}

# Page-specific assets
page_js = {
    "dashboard": "public/js/dashboard.js"
}

# Form-specific assets
web_include_js = ["website_script.js"]
web_include_css = ["website_style.css"]
```

## Asset Optimization

### Minification

Minification removes unnecessary characters from code without changing functionality:

- Comments removal
- White space removal
- Variable name shortening
- Dead code elimination

### Concatenation

Multiple files are combined into a single file to reduce HTTP requests, improving page load times.

### Cache Busting

Frappe adds version hashes to asset URLs to ensure browsers load the latest versions when files change:

```html
<script src="/assets/js/my_app.min.js?v=abc123"></script>
```

## Building and Rebuilding Assets

### Initial Build

Assets are built when:
- A new app is installed
- The bench is started
- You manually trigger a build

### Manual Builds

You can manually build assets using the bench command:

```bash
# Build all assets
bench build

# Build only for a specific app
bench build --app my_app

# Build assets without minification (for development)
bench build --force --no-minify
```

### Development Mode

In development mode, you can enable features to make debugging easier:

```bash
# Enable development mode
bench --site your-site.local set-config developer_mode 1

# Build assets without minification
bench build --force --no-minify
```

This preserves source maps and keeps the code readable for debugging.

## Custom Asset Management

### Adding Third-Party Libraries

To include third-party libraries:

1. Add the library to your app's `public/js` or `public/css` directory
2. Include it in your hooks configuration

Or you can include it directly via CDN:

```python
# In hooks.py
app_include_js = ["https://cdn.example.com/library.js"]
```

### Dependency Management

For managing dependencies between scripts, use the `app_include_js` list order:

```python
app_include_js = [
    # Dependencies first
    "/assets/js/framework.min.js",
    # Your app's code after dependencies
    "/assets/js/my_app.min.js"
]
```

### Custom Builds

For complex bundling needs, you can create custom build processes by overriding the standard build commands:

```bash
# In package.json
"scripts": {
    "build": "rollup -c rollup.config.js",
    "dev": "rollup -c rollup.config.js -w"
}
```

## Troubleshooting

### Common Issues

1. **Assets not updating**: Clear the cache and rebuild
   ```bash
   bench clear-cache && bench build
   ```

2. **JavaScript errors**: Check the browser console for errors

3. **CSS not applying**: Verify the CSS bundle is included correctly and check for specificity issues

4. **Build errors**: Check the Rollup/webpack error output and fix the reported issues

### Asset Cleaning

To clean up old or corrupted assets:

```bash
bench clear-assets
bench build
```

## Best Practices

1. **Organize assets logically**: Group related files together
2. **Use modular JavaScript**: Break code into reusable modules
3. **Minimize dependencies**: Only include what you need
4. **Optimize images**: Compress images before adding them to your app
5. **Use SCSS for complex styles**: Leverage variables, mixins, and nesting for maintainable CSS
6. **Lazy load when possible**: Load non-critical assets only when needed
7. **Monitor bundle sizes**: Keep an eye on the size of your bundles to prevent performance issues

## Conclusion

Frappe's asset bundling system provides a powerful way to manage and optimize your application's front-end assets. By understanding how the system works and following best practices, you can ensure your application loads quickly and performs well for users.