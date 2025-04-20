# UI Integration Testing

You can write integration tests using **Cypress**. It is a NodeJS-based full-stack testing framework that doesn't rely on Selenium.

To write integration tests, create a `.js` file in the `cypress/integration` directory.

---

## Example

Here is an example of an integration test to check the insertion of a To Do:

```javascript
context('ToDo', () => {
  before(() => {
    cy.login('Administrator', 'admin');
    cy.visit('/desk');
  });

  it('creates a new todo', () => {
    cy.visit('/app/todo/new-todo-1');
    cy.fill_field('description', 'this is a test todo', 'Text Editor').blur();
    cy.get('.page-title').should('contain', 'Not Saved');
    cy.get('.primary-action').click();
    cy.visit('/desk#List/ToDo');
    cy.location('hash').should('eq', '/app/todo');
    cy.get('.list-row').should('contain', 'this is a test todo');
  });
});
```

---

## Running Cypress Locally

Cypress uses any Chromium-based browser installed on your system to run tests. Every app has its own Cypress test suite.

### Example: Running Tests for the `frappe` App

Run the following commands:

```bash
cd ~/frappe-bench/apps/frappe
yarn cypress:open
```

This will open the Cypress Electron shell where you can run any test manually or run all of the tests.

---

Was this article helpful? Let us know your feedback!