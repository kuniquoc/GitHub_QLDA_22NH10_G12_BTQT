# Google Calendar Integration

Frappe provides integration with Google Calendar to synchronize events.

## Setup

1. Create a new project on [Google Cloud Platform](https://console.cloud.google.com) and generate OAuth 2.0 credentials.
2. Add your site URL to Authorized JavaScript origins.
3. Add your site URL with the path `?cmd=frappe.integrations.doctype.gcalendar_settings.gcalendar_settings.google_callback` as an authorized redirect URI.
4. Add your Client ID and Client Secret in `Modules > Integrations > Google Calendar > GCalendar Settings`.

## Features

- **Event Synchronization**:
  - Events created in Frappe are created in Google Calendar.
  - Events modified in Frappe are updated in Google Calendar.
  - Events deleted in Frappe are deleted in Google Calendar.
  - Recurring events are supported.
  - Optionally, add a Google Meet conference link to events.

- **User Accounts**:
  - Each user can create their own account in `Google Calendar > GCalendar Account`.
  - Users must authorize the application to access their calendar information.