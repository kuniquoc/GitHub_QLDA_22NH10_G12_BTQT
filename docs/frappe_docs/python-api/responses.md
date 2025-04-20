# Responses




This space has
				{{ pending_patches_count }} change(s) pending for
				review.
			
Review changes



Responses



Here, let's take a look into how responses are built in Frappe, and how you may
be able to use them in your Frappe apps or scripts.
If you have already gone through the Router
Documentation, you might've noticed the
build_response function that Frappe internally utilizes to build responses
depending on the type of the content. The logic that defines this behaviour is a
part of the module
frappe.utils.response,
of which build_response is the meat and potatoes.
def build_response(response_type=None):
 if "docs" in frappe.local.response and not frappe.local.response.docs:
 del frappe.local.response["docs"]

 response_type_map = {
 "csv": as_csv,
 "txt": as_txt,
 "download": as_raw,
 "json": as_json,
 "pdf": as_pdf,
 "page": as_page,
 "redirect": redirect,
 "binary": as_binary,
 }

 return response_type_map[frappe.response.get("type") or response_type]()

The above snippet represents the current implementation of build_response
which maps different functions that act as handlers for different content types.
Let's take a deeper look into the response handler for the "download"
response_type in Frappe v13.
def as_raw():
 response = Response()
 response.mimetype = (
 frappe.response.get("content_type")
 or mimetypes.guess_type(frappe.response["filename"])[0]
 or "application/unknown"
 )
 response.headers["Content-Disposition"] = (
 f'{frappe.response.get("display_content_as", "attachment")};'
 f' filename="{frappe.response["filename"].replace(" ", "_")}"'
 ).encode("utf-8")
 response.data = frappe.response["filecontent"]
 return response

Depending on the value of the Content-Disposition header, the browser
receiving the response may behave differently. If unset, the value defaults to
"attachment".
If frappe.response.display_content_as is set to "inline", it indicates
that the content is expected to be displayed inline in the browser, that is, as
a Web page or as part of a Web page, while "attachment" means the contents
are to be downloaded and saved locally.
To create an API endpoint that would directly download the file you require, you
could craft something like the following to download the file directly.
@frappe.whitelist()
def download(name):
 file = frappe.get_doc("File", name)
 frappe.response.filename = file.file_name
 frappe.response.filecontent = file.get_content()
 frappe.response.type = "download"
 frappe.response.display_content_as = "attachment"








Responses

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







