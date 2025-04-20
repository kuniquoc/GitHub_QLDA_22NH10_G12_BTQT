# Realtime (socket.io)

Frappe ships with an API for realtime events based on [socket.io](https://socket.io/). Since socket.io needs a Node server to run, we run a Node process in parallel to the main web server.

## Client APIs (JavaScript)

### `frappe.realtime.on`
To listen to realtime events on the client (browser), you can use the `frappe.realtime.on` method:

```javascript
frappe.realtime.on('event_name', (data) => {
    console.log(data);
});
```

### `frappe.realtime.off`
Stop listening to an event you have subscribed to:

```javascript
frappe.realtime.off('event_name');
```

## Server APIs (Python)

### `frappe.publish_realtime`
To publish a realtime event from the server, you can use the `frappe.publish_realtime` method:

```python
frappe.publish_realtime('event_name', data={'key': 'value'})
```

### `frappe.publish_progress`
You can use this method to show a progress bar in a dialog:

```python
frappe.publish_progress(25, title='Some title', description='Some description')
```

## Custom Event Handlers

> **Note:** This feature is only available in nightly (v16) version. This feature is considered experimental.

You can implement custom real-time event handlers by creating a `handlers.js` file in the `realtime` folder of your app. You need to specify a single export from this file - a function that will set up event handlers on the socket instance.

For example, if you are developing an app called "chat", here's how the file should look:

```javascript
// bench/apps/chat/realtime/handlers.js

function chat_app_handlers(socket) {
    socket.on("hello_chat", () => {
        console.log("hello world!");
    });
}

module.exports = chat_app_handlers;
```

You can trigger this event using client-side code:

```javascript
frappe.realtime.emit("hello_chat");
```

> Note: You might have to restart the socket.io server to see the effect of code changes. Refer to the [Socket.IO documentation](https://socket.io/docs/v4/) to learn more about writing custom event handlers.

## Custom Client

You can write a custom client to connect to the [socket.io](https://socket.io/) server if you're developing a SPA or a mobile app that doesn't use the Desk interface. You can refer to the official [socket.io documentation](https://socket.io/docs/v4/client-initialization/) for building your custom client.

Here are some examples of custom clients:
- [Example 1](https://github.com/frappe/gameplan/blob/9f9332cf29496afe5e912e4f1734fbf1142cb18c/frontend/src/socket.js#L13)
- [Example 2](https://github.com/frappe/frappe/blob/8093a1d0a54900fe4b43b01ae6ffc0adf855da43/frappe/public/js/frappe/socketio_client.js#L49)

## Authorization in Custom Clients

There are two ways to authenticate a connection with the `socket.io` server:

1. **Cookies**: If your custom client is in a browser-like environment, your connection will automatically send cookies, and the socket.io server will be able to authenticate using the cookies.
2. **Authorization Header**: If cookies are not available in your environment (e.g., mobile apps), you can use Authorization headers just like API requests. Refer to the [REST API authentication documentation](https://frappeframework.com/docs/user/en/api/rest#authentication) and [Socket.IO client options](https://socket.io/docs/v4/client-options/#extraheaders) for more details.

## Implementation Notes

- The realtime server uses the [socket.io](https://socket.io/) server. The server is written in Node.js and can be found in the `/realtime` directory.
- The realtime client is a wrapper around the `socket.io` client library and can be found in `public/js/frappe/socketio_client.js`.
- Python processes publish events to the Node server using the Redis pub-sub channel. The realtime server subscribes to the Redis channel and publishes it to all subscribed clients.
- The realtime server is multi-tenant. All site-related traffic is namespaced by sitename. Namespaces are dynamically created using the `/{sitename}` format, where `sitename` is the name of the site's folder in the `sites` directory or `frappe.local.site`.
- The realtime server uses the main Frappe web server to authenticate connections. The SID cookie or authorization header is passed to the client, and the realtime server uses it to ensure that the connection is from a valid user and can subscribe to certain DocType or documents based on permissions.

### Realtime Implementation Rooms

- **all**: Room accessible and connected by default to all System Users.
- **website**: Room accessible and connected by any user, even Guests.
- **user:{username}**: Dynamic room created for each user. Allowed without any permission checks.
- **doctype:{doctype}**: Dynamic room created for each DocType. Only users with permission to the DocType can join said room. Users are automatically subscribed to this room when they open the list view or form view of the document.
- **doc:{doctype}/{name}**: Dynamic room created for each document. Only users with permission to the document room can join said room. Users are automatically subscribed to this room when they open the form view of the document.