# Web Form

Frappe provides an easy way to generate forms for your website with very little configuration. These forms may be public (anyone can fill them up) or can be configured to require login.

---

## Creating a Web Form

To create a Web Form, follow these steps:

1. Type "new web form" in the awesomebar and hit enter.
2. Enter the **Title**.
3. Select the **DocType** for which the record should be created.
4. Add some **Introduction** (optional).
5. Click on the **Get Fields** button to fetch all fields from the selected DocType or manually select fields for your web form.
6. Publish the form, and you're good to go.

---

## Standard Web Forms

If you check the **Is Standard** checkbox:
- A new folder will be created in the module of the Web Form.
- This folder will contain `.py` and `.js` files that you can use to configure the web form.
- These files need to be checked into version control with your custom app.
- You can install this app on any site, and it will have this web form installed.

**Note**: The **Is Standard** field will only be visible when you are in developer mode.

---

Was this article helpful? Let us know your feedback!