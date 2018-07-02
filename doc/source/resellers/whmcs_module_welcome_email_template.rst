WHMCS module Welcome Email template update
==========================================

The OnePortal module for WHMCS update includes a “OnePortal Welcome” email
template to replace the default WHMCS “Dedicated/VPS Server Welcome Email.”
The default template included in WHMCS assumes that all servers are licensed
with WHM. This white-label template included in the OnePortal module update
works with any server.

**Adding the OnePortal Welcome replacement template**

1. In WHMCS Admin, navigate to Setup->Email Templates
2. Create New Email Template Type: Product/Service
3. Name the template “OnePortal Welcome” or another Unique Name
4. Enter a subject of “New Server Information” or similar
5. Click “Enable/Disable Rich-Text Editor” so that rich-text is disabled
6. Open the oneportal_welcome_text.txt file
7. Copy and paste the plain text from oneportal_welcome_text.txt into the new
   email
8. Save Changes
9. If you have already created the products in WHMCS for the OnePortal module:

 1. For each server, in Setup->Products/Services->Products/Services, select to
    edit the product
 2. In the Details tab, change the Welcome Email to “OnePortal Welcome” or the
    unique name you created for the new template
 3. Save Changes

10. If you have not yet created the products in WHMCS:

 1. When creating each server, under the Details tab, ensure that “OnePortal
    Welcome” or the unique name of the new template is selected

**Ensuring the Merge Fields are filled correctly on the template (additional
required steps for WHMCS 6.2 or earlier)**

1. For each dedicated server or cloud server you sell through the OnePortal
   WHMCS module, create a server in Setup->Products/Services->Servers->Add New
   Server

 1. For Name, enter whatever you would like (easiest to enter server Hostname)
 2. For Hostname, enter the server Hostname
 3. For IP Address, enter the primary IP Address of the server
 4. For Assigned IP Addresses, enter all of the IP Addresses of the server,
    including the primary IP Address (one per line)
 5. Monthly Cost, Datacenter/NOC, and Server Status Address are optional fields
    (they are irrelevant to the email template)
 6. Maximum No. of Accounts is recommended to be “1”
 7. Fill in the Primary Nameserver and Secondary Nameserver fields
 8. In Server Details, for Type, choose Oneportal
 9. Username – “root”
 10. Password – enter root password of server
 11. Save Changes

2. Go to the Client Profile for your new server order, under the
   Products/Services tab
3. For Server, select the server created in Step 1 from the dropdown list
4. Save Changes

Now the product welcome email will appear similar to:

.. image:: /image/whmcs_email_template.png

.. disqus::
