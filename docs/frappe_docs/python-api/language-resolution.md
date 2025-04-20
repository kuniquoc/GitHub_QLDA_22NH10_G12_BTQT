# Language Resolution

This document explains how language is resolved in Frappe and how you can use it in your Frappe apps or scripts.

## Language Resolution Order

The language for your session depends on the value of `frappe.lang`. This is resolved in the following order:

1. **Form Dict > `_lang`**  
   The `_lang` parameter in the Form Dict has the highest priority. Setting this will update all translatable components in the given request. Frappe uses this mechanism in certain places to handle Email Templates and Print views.

2. **Cookie > `preferred_language`**  
   If `_lang` is not set, the `preferred_language` key in cookies is checked. This method is used for the website language switcher and persists language settings temporarily.  
   > **Note:** This is only considered for Guest Users and ignored for logged-in users.

3. **Request Header > `Accept-Language`**  
   If neither `_lang` nor `preferred_language` is set, Frappe resolves the `Accept-Language` header. This header contains an ordered set of acceptable languages sent by the client.  
   > **Note:** This is only considered for Guest Users and ignored for logged-in users.  
   For more details, refer to [Mozilla Docs on Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language).

4. **User Document > `language`**  
   If the above methods are not set, the `language` field in the User document is used. This setting persists across devices and clients, allowing users to view the website and Desk in their preferred language.

5. **System Settings > `language`**  
   If no other language is set, the `language` field in System Settings is used as the fallback language for all sessions.

---

## Detailed Explanation of Each Method

### Form Dict: `_lang`
The `_lang` parameter in the Form Dict is the most immediate way to set the language for a session. It is often used for specific requests like rendering Email Templates or Print views.

#### Example
```python
frappe.form_dict._lang = "fr"
```

---

### Cookie: `preferred_language`
Setting the `preferred_language` key in cookies allows for a persistent yet temporary language setting. This is commonly used for website language switchers.

#### Example
```javascript
document.cookie = "preferred_language=fr";
```

> **Note:** This method is ignored for logged-in users.

---

### Request Header: `Accept-Language`
The `Accept-Language` header is a standard way to manage language preferences. It is sent by the client and contains an ordered list of acceptable languages.

#### Example
```
Accept-Language: en-US,en;q=0.9,fr;q=0.8
```

> **Note:** This method is ignored for logged-in users.

---

### User & System Settings
- **User Document > `language`**:  
  The `language` field in the User document sets the session language for the user. This setting persists across devices and clients. For example, if a user sets their language to "Russian" on a "French" site, the site will automatically translate to Russian upon login.

- **System Settings > `language`**:  
  The `language` field in System Settings sets the default language for the entire site. It has the lowest priority and acts as a fallback.

---

## Summary

The language resolution in Frappe follows a hierarchical order, starting from the most specific (Form Dict) to the most general (System Settings). This ensures flexibility and customization for both users and developers.
