# Running Background Jobs

Sometimes you may not want a user request to be executed immediately but added to a queue that will be executed by a background worker. The advantage of doing this is that your web workers remain free to execute other requests, and longer jobs do not eat up all of your resources.

## Using Python RQ

Frappe uses Python RQ to run background jobs. The following example illustrates how you can enqueue a job:

```python
import frappe

def long_job(arg1, arg2):
    frappe.publish_realtime('msgprint', 'Starting long job...')
    # this job takes a long time to process
    frappe.publish_realtime('msgprint', 'Ending long job...')

def enqueue_long_job(arg1, arg2):
    frappe.enqueue('myapp.mymodule.long_job', arg1=arg1, arg2=arg2)
```

This will enqueue `long_job` to the queue `default`. Other available queues are `long` and `short`. Choose the appropriate queue based on how long you estimate your enqueued job to execute.

## Delayed Actions on Document Objects

You can also call delayed actions on document objects. For example, in Stock Reconciliation, if there are more than 100 items, it is executed as a background job.

```python
def submit(self):
    if len(self.items) > 100:
        self.queue_action('submit')
    else:
        self._submit()
```