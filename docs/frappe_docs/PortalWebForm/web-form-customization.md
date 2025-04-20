# Web Form Customization

You can customize your web form to make it more unique and enable functionalities to meet your use case.

---

## Customization Options

### 1. **Fields Layout**
- Add **Column Breaks** and **Section Breaks** in the fields table to change the layout of the form fields.

### 2. **Multi-Step Web Form**
- Use **Page Breaks** to divide the form into multiple pages (maximum 10 pages).

### 3. **Submit Button Label**
- Change the label of the submit button on the web form.

### 4. **Banner Image**
- Add a banner image to the web form.

### 5. **Breadcrumbs**
- Customize breadcrumbs by adding a JSON object.
- Breadcrumbs are visible only if the web form **List View** is enabled.

### 6. **After Submit Page**
- Configure a custom success title and message to display after the form is submitted.
- Redirect users to a specific URL after submission using the `success_url` field.

### 7. **Custom CSS**
- Add custom CSS to change the look of the web form.

---

## Client Script

You can add a custom client script to the web form for additional functionality.

### Examples:

#### 1. Show a Message on Startup
```javascript
frappe.web_form.after_load = () => {
    frappe.msgprint('Please fill all values carefully');
};
```

#### 2. Custom Validation
```javascript
frappe.web_form.validate = () => {
    let data = frappe.web_form.get_values();
    if (data.amount < 1000) {
        frappe.msgprint('Value must be more than 1000');
        return false;
    }
};
```

#### 3. Hide a Field Based on Value
```javascript
frappe.web_form.on('amount', (field, value) => {
    if (value < 1000) {
        frappe.web_form.set_df_property('rate', 'hidden', 1);
    }
});
```

---

Was this article helpful? Let us know your feedback!