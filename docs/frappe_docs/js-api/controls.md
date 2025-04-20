# Controls




This space has
				{{ pending_patches_count }} change(s) pending for
				review.
			
Review changes



Controls



frappe.ui.form.make_control
frappe.ui.form.make_control({ parent, df })
Makes a frappe control based on df properties and appends into parent
container.
frappe.ui.form.make_control({
 parent: $wrapper.find('.my-control'),
 df: {
 label: 'Due Date',
 fieldname: 'due_date',
 fieldtype: 'Date'
 },
 render_input: true
})

Here are the df properties for most of frappe control types.
// Attach
{
 label: 'Attachment',
 fieldname: 'attachment',
 fieldtype: 'Attach'
}

// Attach Image
{
 label: 'User Image',
 fieldname: 'user_image',
 fieldtype: 'Attach Image'
}

// Autocomplete
{
 label: 'Select User',
 label: 'user',
 fieldtype: 'Autocomplete',
 options: [
 'faris@erpnext.com',
 'suraj@erpnext.com'
 ]
}

// Barcode
{
 label: 'Item Barcode',
 fieldname: 'item_barcode',
 fieldtype: 'Barcode'
}

// Check
{
 label: 'Enable feature',
 fieldname: 'enable_feature',
 fieldtype: 'Check'
}

// Code
{
 label: 'JS Script',
 fieldname: 'script',
 fieldtype: 'Code',
 // for syntax highlighting
 options: 'Javascript' // JS, HTML, CSS, Markdown, SCSS, JSON,
 // wrap code
 wrap: true,
 // changing `max_lines` will set the max-height of the editor
 max_lines: 10,
 // changing `min_lines` will set the min-height of the editor
 min_lines: 5
}

// Color
{
 label: 'Your favorite color',
 fieldname: 'user_color',
 fieldtype: 'Color'
}

// Currency
{
 label: 'Amount',
 fieldname: 'amount',
 fieldtype: 'Currency',
 options: 'INR' // or name of field which holds currency
}

// Data
{
 label: 'First Name',
 fieldname: 'first_name',
 fieldtype: 'Data',
 options: 'Email' // 'Name', 'Phone', 'URL', 'Barcode'
}

// Date Range
{
 label: 'Select Date Range',
 fieldname: 'date_range',
 fieldtype: 'Date Range'
}

// Date
{
 label: 'Birth Date',
 fieldname: 'birth_date',
 fieldtype: 'Date'
}

// Datetime
{
 label: 'Submission Date and Time',
 fieldname: 'submission',
 fieldtype: 'Datetime'
}

// Dynamic Link
{
 label: 'Party',
 fieldname: 'party',
 fieldtype: 'Dynamic Link',
 options: 'party_type' // fieldname which holds the Link type
}

// Float
{
 label: 'Threshold',
 fieldname: 'threshold',
 fieldtype: 'Float'
}

// Geolocation
{
 label: 'Meeting Place',
 fieldname: 'meeting_place',
 fieldtype: 'Geolocation'
}

// HTML Editor
{
 label: 'Custom HTML',
 fieldname: 'custom_html',
 fieldtype: 'HTML Editor'
}

// Int
{
 label: 'No of days',
 fieldname: 'no_of_days',
 fieldtype: 'Int'
}

// Link
{
 label: 'Select User',
 fieldname: 'user',
 fieldtype: 'Link',
 options: 'User' // name of doctype
}

// Markdown Editor
{
 label: 'Blog Content',
 fieldname: 'content',
 fieldtype: 'Markdown Editor'
}

// MultiCheck
{
 label: 'Blog Content',
 fieldname: 'content',
 fieldtype: 'MultiCheck',
 options: [
 'Option 1',
 'Option 2',
 'Option 3',
 'Option 4',
 ],
 columns: 2 // break into 2 columns
}

// MultiSelect
{
 label: 'Select Users',
 fieldname: 'users',
 fieldtype: 'MultiSelect',
 options: [
 'faris@erpnext.com',
 'suraj@erpnext.com',
 'shivam@erpnext.com'
 ]
}

// Password
{
 label: 'New Password',
 fieldname: 'password',
 fieldtype: 'Password'
}

// Rating
{
 label: 'Rate your experience',
 fieldname: 'rating',
 fieldtype: 'Rating'
}

// Select
{
 label: 'Status',
 fieldname: 'status',
 fieldtype: 'Select',
 options: [
 'Open',
 'Closed',
 'Cancelled'
 ]
}

// Signature
{
 label: 'Status',
 fieldname: 'status',
 fieldtype: 'Signature'
}

// Text Editor
{
 label: 'Description',
 fieldname: 'description',
 fieldtype: 'Text Editor'
}

// Time
{
 label: 'In Time',
 fieldname: 'in_time',
 fieldtype: 'Time'
}

// Button
{
 label: 'Fetch',
 fieldname: 'fetch',
 fieldtype: 'Button',
 btn_size: 'xs' // xs, sm, lg
}

//Icon
{
 label: 'Page Icon',
 fieldname: 'page_icon',
 fieldtype: 'Icon'
}

Adding Custom Formatters
You can add custom formatters for text type objects (Data, Select, Text etc) by adding them to the docfield object in frappe.meta.docfield_map
Example:
frappe.meta.docfield_map['DocField'].fieldtype.formatter = (value) => {
 if (value==='Section Break') return '🔵 Section Break';
 else return value;
}








Controls

administrator edited 4 months ago


×




No Revisions



Previous
Next








Page Settings

×





Route


                                framework/
                            






                            Hide on Sidebar
                        





                    Update
                








    Preview
  


      Discard
    


        Save
      

Toggle Dropdown


Draft







Title


Content






















































































Title


Enter title for the new Wiki Group



Submit





Was this article helpful?
Give Feedback





Feedback

×



How would you rate this page?



                            1
                        

                            2
                        

                            3
                        

                            4
                        

                            5
                        


How can we make it better?



                    Submit
                













Edit Page
New Page

				Revisions
			

				Page Settings
			






Previous Page
Left


Next Page
Right







