# Static Assets

## Introduction to Static Assets

Static assets in Frappe refer to files that don't change during the runtime of the application and are served directly to the client. These include:

- JavaScript files (.js)
- Cascading Style Sheets (.css)
- Images (.png, .jpg, .gif, .svg)
- Fonts (.woff, .woff2, .ttf, .eot)
- JSON files (.json)
- Other media files

These static assets are crucial for the functionality and appearance of your application, providing the necessary styles, interactivity, and resources for users.

## Asset Organization

In Frappe, static assets are organized within each app's directory structure:

```
my_custom_app/
└── my_custom_app/
    ├── public/
    │   ├── js/
    │   │   └── my_script.js
    │   ├── css/
    │   │   └── my_style.css
    │   ├── scss/
    │   │   └── my_scss_file.scss
    │   └── images/
    │       └── logo.png
    └── ...
```

When the application is built, these assets are processed and copied to a central assets directory under the `sites` folder:

```
sites/
├── assets/
│   ├── my_custom_app/
│   │   ├── js/
│   │   ├── css/
│   │   └── images/
│   └── ...
└── ...
```

## Asset URL Structure

In Frappe, static assets are accessed through URLs with the following pattern:

```
/assets/[app_name]/[path_to_asset]
```

For example, an image file located at `my_custom_app/public/images/logo.png` would be accessed via:

```
/assets/my_custom_app/images/logo.png
```

## Including Static Assets in Templates

### In Jinja Templates

You can include static assets in your Jinja templates using the `{{ assets_json }}` variable:

```html
<img src="{{ assets_json.my_custom_app }}/images/logo.png" alt="Logo">
```

Or using the more direct method:

```html
<img src="/assets/my_custom_app/images/logo.png" alt="Logo">
```

### In JavaScript

In JavaScript files, you can reference static assets using the `frappe.assets_json` object:

```javascript
const logoUrl = frappe.assets_json.my_custom_app + '/images/logo.png';
$('<img>').attr('src', logoUrl).appendTo('#logo-container');
```

Or by using the direct URL path:

```javascript
const logoUrl = '/assets/my_custom_app/images/logo.png';
```

## Asset Handling in Development vs Production

### Development Mode

In development mode:
- Assets are served without minification
- Files are not aggressively cached
- Source maps are available for easier debugging

### Production Mode

In production mode:
- Assets are minified and optimized
- Long-term caching is applied with version hashes
- Source maps are typically omitted

## Working with Different Asset Types

### JavaScript Files

JavaScript files are placed in the `public/js` directory and can be included in your application through the `hooks.py` file:

```python
# In hooks.py
app_include_js = ["/assets/my_custom_app/js/my_script.js"]
```

### CSS Files

CSS files are placed in the `public/css` directory and can be included similarly:

```python
# In hooks.py
app_include_css = ["/assets/my_custom_app/css/my_style.css"]
```

### SCSS Files

SCSS files are placed in the `public/scss` directory and are automatically compiled to CSS during the build process:

```scss
// public/scss/my_style.scss
$primary-color: #4287f5;

.my-element {
  color: $primary-color;
  font-weight: bold;
}
```

### Images and Other Media

Images and other media files can be placed in appropriate subdirectories under `public/`:

```
public/
├── images/
├── fonts/
└── videos/
```

## Asset Versioning and Caching

Frappe implements asset versioning to enable efficient browser caching. When an asset is built, a version hash is added to the URL:

```html
<script src="/assets/my_custom_app/js/my_script.js?v=abc123"></script>
```

This ensures that when you update an asset, browsers will download the new version rather than using the cached version.

## Custom Asset Handlers

For specialized asset handling, you can define custom routes in `hooks.py`:

```python
website_route_rules = [
    {"from_route": "/downloads/<path:name>", "to_route": "download_handler"}
]
```

Then create a corresponding Python function to handle these requests:

```python
@frappe.whitelist(allow_guest=True)
def download_handler(name):
    # Custom logic for handling downloads
    file_path = os.path.join(frappe.get_app_path("my_custom_app", "downloads"), name)
    with open(file_path, "rb") as f:
        content = f.read()
    
    frappe.response["filecontent"] = content
    frappe.response["type"] = "download"
    frappe.response["filename"] = name
```

## Optimizing Static Assets

### Image Optimization

Optimize images before adding them to your app:
- Use appropriate formats (JPEG for photos, PNG for graphics with transparency, SVG for icons)
- Compress images using tools like ImageOptim, TinyPNG, or compression libraries
- Consider using responsive images with different sizes for different devices

Example of responsive images in HTML:

```html
<picture>
  <source srcset="/assets/my_custom_app/images/logo-large.png" media="(min-width: 1200px)">
  <source srcset="/assets/my_custom_app/images/logo-medium.png" media="(min-width: 768px)">
  <img src="/assets/my_custom_app/images/logo-small.png" alt="Logo">
</picture>
```

### CSS Optimization

- Use CSS methodologies like BEM (Block Element Modifier) to avoid specificity issues
- Split CSS into logical modules
- Utilize SCSS features for maintainable styles:
  - Variables for repeated values
  - Mixins for reusable style patterns
  - Nesting for logical hierarchy

### JavaScript Optimization

- Split code into modular, reusable components
- Load non-critical JavaScript asynchronously
- Use ES6+ features with appropriate polyfills for older browsers

## Best Practices

1. **Use appropriate file organization**: Place files in logical directories (js/, css/, images/)
2. **Optimize all assets before committing**: Minify and compress assets to reduce file size
3. **Use meaningful filenames**: Name files descriptively for easier maintenance
4. **Cache effectively**: Leverage Frappe's versioning system for optimal caching
5. **Use asset preloading for critical resources**:
   ```html
   <link rel="preload" href="/assets/my_custom_app/fonts/main-font.woff2" as="font" type="font/woff2" crossorigin>
   ```
6. **Follow proper asset bundling**: Group related assets together
7. **Consider lazy loading**: Load non-critical assets only when needed
8. **Use web-optimized formats**: WebP for images, WOFF2 for fonts
9. **Test loading performance**: Use browser developer tools to identify bottlenecks

## Conclusion

Static assets are fundamental to creating functional, visually appealing Frappe applications. By understanding how to organize, include, and optimize your static assets, you can improve both the user experience and performance of your application.