# Unit Testing

Frappe provides some basic tooling to quickly write automated tests. There are some basic rules:

1. Tests can be anywhere in your repository but must begin with `test_` and should be a `.py` file.
2. Tests must run on a site that starts with `test_`. This is to prevent accidental loss of data.
3. Test stubs are automatically generated for new DocTypes.
4. Frappe test runner will automatically build test records for dependent DocTypes identified by the `Link` type field (Foreign Key).
5. Tests can be executed using `bench run-tests`.
6. For non-DocType tests, you can write simple unittests and prefix your file names with `test_`.

---

## Writing Tests for DocTypes

### 1. Writing DocType Tests
- Test cases are in a file named `test_[doctype].py`.
- You must create all dependencies in the test file.
- Create a Python module structure to create fixtures/dependencies.

#### Example (for `test_event.py`):
```python
# Example test file for Event DocType
import frappe
from frappe.tests.utils import FrappeTestCase

class TestEvent(FrappeTestCase):
    def test_event_creation(self):
        event = frappe.get_doc({
            "doctype": "Event",
            "subject": "Test Event",
            "starts_on": "2025-04-20 10:00:00"
        })
        event.insert()
        self.assertEqual(event.subject, "Test Event")
```

---

## Running Tests

You can run tests from the `frappe_bench` folder. Without options, all tests will be run:
```bash
bench run-tests
```

### Options:
- `--app <appname>`: Run tests for a specific app.
- `--doctype <doctype>`: Run tests for a specific DocType.
- `--test <specifictest>`: Run a specific test case.
- `--module <module>`: Run a particular module that has tests.
- `--profile`: Runs a Python profiler on the test.
- `--junit-xml-output <path>`: Provides test results in the standard XUnit XML format.

#### Examples:
1. Run tests for an app:
   ```bash
   bench run-tests --app erpnext
   ```

2. Run tests for a specific DocType:
   ```bash
   bench run-tests --doctype "Activity Cost"
   ```

3. Run a specific test:
   ```bash
   bench run-tests --doctype User --test test_get_value
   ```

4. Run tests in a module:
   ```bash
   bench run-tests --module "erpnext.stock.doctype.stock_entry.test_stock_entry"
   ```

5. Run tests with profiling:
   ```bash
   bench run-tests --doctype "Activity Cost" --profile
   ```

---

## Skipping Test Records or Initialization

- Use `--skip-test-records` to skip building test dependencies (fixtures for linked objects).
- Use `--skip-before-tests` to skip the test initialization script.

#### Example:
```bash
bench --site school.erpnext.local run-tests --doctype "Student Group" --skip-test-records --skip-before-tests
```

---

## `FrappeTestCase`

`FrappeTestCase` is a Frappe Framework-specific `TestCase` class extended from `unittest.TestCase`. Inheriting this class in your tests ensures:
1. `frappe.local.flags` and other local proxies are reset after the test case runs.
2. A new database transaction is started before the test case begins and rolled back after the test finishes.

#### Example:
```python
from frappe.tests.utils import FrappeTestCase

class TestExample(FrappeTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()  # Important to call super() methods when extending TestCase.
```

---

## Writing XUnit XML Tests

To generate test reports in XUnit XML format:
```bash
bench run-tests --junit-xml-output=/reports/junit_test.xml
```

#### Example of Test Report:
```xml
<testsuite tests="3">
    <testcase classname="foo1" name="ASuccessfulTest"/>
    <testcase classname="foo2" name="AnotherSuccessfulTest"/>
    <testcase classname="foo3" name="AFailingTest">
        <failure type="NotEnoughFoo">details about failure</failure>
    </testcase>
</testsuite>
```

This format is designed for CI tools like Jenkins, but it will work with any tool that understands XUnit-formatted XML test results.

---

## Jenkins Configuration Support

1. Install the [xUnit plugin](https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin).
2. In Jenkins job configuration, enable "Publish JUnit test result report" under "Post-build Actions" and enter the path to the XML report (e.g., `reports/*.xml`).

---

Was this article helpful? Let us know your feedback!