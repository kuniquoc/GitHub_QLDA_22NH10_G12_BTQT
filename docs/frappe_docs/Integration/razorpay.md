# RazorPay Integration

Razorpay is a popular payments solution in India that allows businesses to accept, process, and disburse payments with its product suite. It supports payment methods like Credit Cards, Debit Cards, and Netbanking.

---

## Steps for Integration

### 1. Include Checkout Script in Your Code
Insert the following script on your page:
```html
<script type="text/javascript" src="/assets/js/checkout.min.js"></script>
```
The checkout script automatically fetches the Razorpay checkout script and wraps their API for some syntactic sugar.

---

### 2. Create the Order Controller in Your Backend
Define a method to create an order:
```python
def get_razorpay_order(self):
    controller = get_payment_gateway_controller("Razorpay")

    payment_details = {
        "amount": 30000,
        "reference_doctype": "Conference Participant",
        "reference_docname": self.name,
        "receipt": self.name
    }

    return controller.create_order(**payment_details)
```

---

### 3. Initiate the Payment in Client Using Checkout API
Use the following JavaScript code to initiate the payment:
```javascript
function make_payment(ticket) {
    var options = {
        "name": "<CHECKOUT MODAL TITLE>",
        "description": "<CHECKOUT MODAL DESCRIPTION>",
        "image": "<CHECKOUT MODAL LOGO>",
        "prefill": {
            "name": "<CUSTOMER NAME>",
            "email": "<CUSTOMER EMAIL>",
            "contact": "<CUSTOMER PHONE>"
        },
        "theme": {
            "color": "<MODAL COLOR>"
        },
        "doctype": "<REFERENCE DOCTYPE>", // Mandatory
        "docname": "<REFERENCE DOCNAME>" // Mandatory
    };

    razorpay = new frappe.checkout.razorpay(options);
    razorpay.on_open = () => {
        // SCRIPT TO RUN WHEN MODAL OPENS
    };
    razorpay.on_success = () => {
        // SCRIPT TO RUN ON PAYMENT SUCCESS
    };
    razorpay.on_fail = () => {
        // SCRIPT TO RUN ON PAYMENT FAILURE
    };
    razorpay.init(); // Creates the order and opens the modal
}
```

---

## Lifecycle

1. **Create an Order in Your Backend**
   - An order is created at the server triggered by `razorpay.init()`.
   - The `get_razorpay_order` method sets the amount and a unique receipt ID.
   - This internally calls the `create_order` controller of the Razorpay settings DocType.

2. **Process Checkout at Client**
   - A successful creation of the order returns the `order_id`.
   - The `order_id` is passed to the client, triggering the Razorpay modal.

3. **Verify the Payment**
   - After the payment, depending on the status, the success or fail API method is called, and the payment ID is passed to it.

---

Was this article helpful? Let us know your feedback!