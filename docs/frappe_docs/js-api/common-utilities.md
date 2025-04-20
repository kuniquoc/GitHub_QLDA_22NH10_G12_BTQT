# Common Utilities




This space has
				{{ pending_patches_count }} change(s) pending for
				review.
			
Review changes



Common Utilities API



frappe.get_route
frappe.get_route()
Returns the current route as an array.
frappe.get_route()
// ["List", "Task", "List"]

frappe.set_route
frappe.set_route(route)
Changes the current route to route.
// route in parts
frappe.set_route('List', 'Task', 'List')

// route as array
frappe.set_route(['List', 'Task', 'Gantt'])

// route as string
frappe.set_route('List/Event/Calendar')

// route with options
frappe.set_route(['List', 'Task', 'Task'], { status: 'Open' })

frappe.format
frappe.format(value, df, options, doc)
Format a raw value into user presentable format.
frappe.format('2019-09-08', { fieldtype: 'Date' })
// "09-08-2019"

frappe.format('2399', { fieldtype: 'Currency', options: 'currency' }, { inline: true })
// "2,399.00"

frappe.provide
frappe.provide(namespace)
Creates a namespace attached to the window object if it doesn't exist.
frappe.provide('frappe.ui.form');

// has the same effect as
window.frappe = {}
window.frappe.ui = {}
window.frappe.ui.form = {}

frappe.require
frappe.require(asset_path, callback)
Load a JS or CSS asset asynchronously. It is used for libraries that are not
used often.
// load a single asset
frappe.require('/assets/frappe/chat.js', () => {
 // chat.js is loaded
})

// load multiple assets
frappe.require(['/assets/frappe/chat.js', '/assets/frappe/chat.css'], () => {
 // chat.js and chat.css are loaded
})








Common Utilities API

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







