# Utility Functions

Frappe Framework comes with various utility functions to handle common operations for managing site-specific DateTime management, date and currency formatting, PDF generation, and much more.

These utility methods can be imported from the `frappe.utils` module (and its nested modules like `frappe.utils.logger` and `frappe.utils.data`) in any Python file of your Frappe App. This list is not exhaustive; you can explore the Framework codebase to see what's available.

---

## Date and Time Utilities

### `now`
```python
now()
```
Returns the current datetime in the format `yyyy-mm-dd hh:mm:ss`.

#### Example:
```python
from frappe.utils import now
now()  # '2021-05-25 06:38:52.242515'
```

---

### `getdate`
```python
getdate(string_date=None)
```
Converts `string_date` (`yyyy-mm-dd`) to a `datetime.date` object. If no input is provided, the current date is returned. Throws an exception if `string_date` is invalid.

#### Example:
```python
from frappe.utils import getdate
getdate()  # datetime.date(2021, 5, 25)
getdate('2000-03-18')  # datetime.date(2000, 3, 18)
```

---

### `today`
```python
today()
```
Returns the current date in the format `yyyy-mm-dd`.

#### Example:
```python
from frappe.utils import today
today()  # '2021-05-25'
```

---

### `add_to_date`
```python
add_to_date(date, years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0, as_string=False, as_datetime=False)
```
Adds or subtracts a specific time delta to/from a date.

#### Example:
```python
from datetime import datetime
from frappe.utils import add_to_date

today = datetime.now().strftime('%Y-%m-%d')
print(today)  # '2021-05-21'

after_10_days = add_to_date(datetime.now(), days=10, as_string=True)
print(after_10_days)  # '2021-05-31'
```

---

### `date_diff`
```python
date_diff(date_2, date_1)
```
Returns the difference between two dates in days.

#### Example:
```python
from frappe.utils import add_to_date, today, date_diff
date_1 = today()
date_2 = add_to_date(date_1, days=10)
print(date_diff(date_2, date_1))  # 10
```

---

### `days_diff`
```python
days_diff(date_2, date_1)
```
Returns the difference between two dates in days.

#### Example:
```python
from frappe.utils import add_to_date, today, days_diff
date_1 = today()
date_2 = add_to_date(date_1, days=10)
print(days_diff(date_2, date_1))  # 10
```

---

### `month_diff`
```python
month_diff(date_2, date_1)
```
Returns the difference between two dates in months.

#### Example:
```python
from frappe.utils import add_to_date, month_diff
date_1 = "2024-07-01"
date_2 = add_to_date(date_1, days=60)
print(month_diff(date_2, date_1))  # 2
```

---

### `pretty_date`
```python
pretty_date(iso_datetime)
```
Returns a human-readable string representing how long ago the date represents.

#### Example:
```python
from frappe.utils import pretty_date, now
pretty_date(now())  # 'just now'
```

---

### `format_duration`
```python
format_duration(seconds, hide_days=False)
```
Converts a duration in seconds to a human-readable format.

#### Example:
```python
from frappe.utils import format_duration
format_duration(10000)  # '2h 46m 40s'
```

---

## String Utilities

### `comma_and`
```python
comma_and(some_list, add_quotes=True)
```
Formats a list into a string with commas and "and".

#### Example:
```python
from frappe.utils import comma_and
comma_and([1, 2, 3])  # "'1', '2' and '3'"
```

---

### `money_in_words`
```python
money_in_words(number, main_currency=None, fraction_currency=None)
```
Converts a number into words with currency.

#### Example:
```python
from frappe.utils import money_in_words
money_in_words(900.50, 'USD')  # 'USD Nine Hundred and Fifty Cents only.'
```

---

### `validate_json_string`
```python
validate_json_string(string)
```
Validates if a string is a valid JSON.

#### Example:
```python
from frappe.utils import validate_json_string
validate_json_string('[]')  # No exception
```

---

### `random_string`
```python
random_string(length)
```
Generates a random string of the specified length.

#### Example:
```python
from frappe.utils import random_string
random_string(6)  # 'htrB4L'
```

---

### `unique`
```python
unique(seq)
```
Removes duplicates from a sequence while preserving order.

#### Example:
```python
from frappe.utils import unique
unique([1, 2, 3, 1])  # [1, 2, 3]
```

---

## PDF Utilities

### `get_pdf`
```python
get_pdf(html, options=None, output=None)
```
Generates a PDF from HTML.

#### Example:
```python
from frappe.utils.pdf import get_pdf
html = '<h1>Invoice</h1>'
pdf = get_pdf(html)
```

---

## Email Utilities

### `sendmail`
```python
sendmail(recipients=[], sender="", subject="", message="", **kwargs)
```
Sends an email.

#### Example:
```python
import frappe
frappe.sendmail(
    recipients=['example@domain.com'],
    subject='Test Email',
    message='Hello, this is a test email.'
)
```

---

## Cache Utilities

### `frappe.cache`
```python
cache()
```
Returns the Redis connection for caching.

#### Example:
```python
import frappe
cache = frappe.cache()
cache.set('key', 'value')
cache.get('key')  # 'value'
```

---

## File Locking

### `filelock`
```python
filelock(name)
```
Synchronizes processes to avoid race conditions.

#### Example:
```python
from frappe.utils.synchronization import filelock
with filelock("config_name"):
    # Critical section
    pass
```