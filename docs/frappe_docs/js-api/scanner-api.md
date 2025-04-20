# Scanner Api




This space has
				{{ pending_patches_count }} change(s) pending for
				review.
			
Review changes



Scanner API



Frappe uses the open-source library Html5-QRCode to provide a flexible way to handle inputs like Barcodes, QRCodes, etc. using the device camera.
frappe.ui.Scanner
new frappe.ui.Scanner({ ... })

Creates a new Scanner instance that can be used to scan single or multiple barcodes.
Options:

container: Dom element under which video feed from the camera will be shown.
dialog: If set as true, will open a dialog to show video feed from the camera.
multiple: If set as false, will stop scanning after one successful scan.
on_scan: Callback method to handle the scanned input.

Here is a sample client code to scan one single barcode and log it to the console.
new frappe.ui.Scanner({
 dialog: true, // open camera scanner in a dialog
 multiple: false, // stop after scanning one value
 on_scan(data) {
 console.log(data.decodedText);
 }
});

The below code can be used to continously scan and handle the scanned input.
const scanner = new frappe.ui.Scanner({
 dialog: true, // open camera scanner in a dialog
 multiple: true, // stop after scanning one value
 on_scan(data) {
 handle_scanned_barcode(data.decodedText);
 }
});

To stop the scanning, you can either close the dialog or use scanner.stop_scan();







Scanner API

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







