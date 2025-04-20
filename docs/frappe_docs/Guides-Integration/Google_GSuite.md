# Google GSuite

Frappe allows you to use Google GSuite documents as templates. You can generate new GSuite documents populated with data from your DocType using the Jinja2 format. The generated document is attached to the DocType as an attachment.

## Steps to Enable Integration

1. **Publish Google Apps Script**
   - Go to [Google Apps Script](https://script.google.com) and create a new project.
   - Deploy the app as a web app.

2. **Get Google Access**
   - Go to the [Google Project Console](https://console.developers.google.com) and enable the Google Drive API.
   - Create OAuth credentials and add the redirect URI.

3. **Associate Template to a DocType**
   - Go to `Integrations > GSuite Templates > New`.
   - Fill in the template name, related DocType, template ID, and destination folder ID.

4. **Generate Documents**
   - Go to a document in the related DocType.
   - Click on "Attach File" and select the template.