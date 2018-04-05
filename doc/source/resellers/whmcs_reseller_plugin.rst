WHMCS Reseller Modules – Best Practices
=======================================


This article presents some best practices with regard to configuring WHMCS
to work with the Limestone Networks API modules for remote server
administration. Any information contained in this article is meant to serve as
an auxiliary resource and is not a substitute for the installation instructions
included in the `official Github repository
<https://github.com/limestonenetworks/oneportal-whmcs>`.

**Dedicated Servers – Best Practices**

When getting started with `dedicated servers
<https://www.limestonenetworks.com/dedicated-servers/bare-metal.html>`, it is
recommended to use the Opserverimport Addon module in conjunction with the
OnePortal server module, as this combination provides the ability to create a
complete replication of all products and configurable options available in a
matter of seconds. For those who are looking to further customize a more unique
offering, the aforementioned module combination is still highly recommended as
a time-saver since deactivating or hiding products and configurable options can
be accomplished very quickly using the native WHMCS web-interface or, for those
serious WHMCS admins, by modifying the database tables directly.

All products and options are assigned default prices which mirror the LSN
website pricing. Partners and resellers are encouraged to modify price and any
other aspects as per their business requirements.

**Cloud Servers – Best Practices**

When adding cloud servers as products, it is best to consider how you plan to
display them on your site. The “cloud slider” is a popular interactive display,
which allows your clients to choose between 3-6 different preconfigured cloud
instances before making the next step to configurable options, where they can
further customize the cloud server resources to their specific needs.

Initially, when adding the configurable options for cloud servers, adding all
available configurable options to one configurable options list is recommended.
Then duplicate the list for each different preconfigured server you are going
to display and tick the boxes to hide each irrelevant option. Adjust the
pricing for the remaining options accordingly (i.e. if your preconfigured
server has 2 cores, 4GB RAM, & 60GB SSD drive, you would hide the options for
1 core, 2GB RAM, 40 GB SSD, etc. as they are irrelevant to this preconfigured
server). Ultimately, this will be entirely up to you to customize.

**How the API Interacts**

For *dedicated servers*, when an order is placed through your website, the
WHMCS API module does not provide automatic product "provisioning", as all
servers are custom-built and tested by server technicians to ensure quality and
accuracy. In an effor to provide consistent, high-quality server hosting, a
quick trip to the Limestone Networks server order form is required. When the
server is live, you are notified in your OnePortal account and via email.
Generally, this is within 1-4 hours of the server being ordered at our website.

We are always working to improve the workflow, so as to better suit our
partners, so we do appreciate any suggestions and feedback from resellers.

With *cloud servers*, utility-style billing methods are employed to make
instant provisioning of your cloud a reality. When our system receives an
order, our API will automatically provision the new server to your client
through your account on an hourly billing basis. In order for this process to
start, the OnePortal account must have a minimum of $5.00 USD balance in the
Cloud pool.

**Bonus Content**

Partners are welcome to contact us via OnePortal ticket to have the invoice
converted to monthly billing, if desired.

Regarding support, partners of Limestone Networks will act as the first line
of support to their clients. However, you may pass support requests to us on
behalf of your clients. Please contact the sales department with any questions
you have regarding the Reseller Program, the tools available, or to receive a
server quote for your custom requirements.
