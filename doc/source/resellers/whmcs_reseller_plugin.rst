WHMCS Reseller Plugin – Best Practices
======================================

Link to download WHMCS plugin & installation instructions: `https://github.com/limestonenetworks/oneportal-whmcs <https://github.com/limestonenetworks/oneportal-whmcs>`_


This article presents some best practices with regard to configuring the WHMCS plugin that is available through the reseller program. Any information contained in this article is meant to serve as an auxiliary resource and is not a substitute for the installation instructions included on the GitHub download page.

**Dedicated Servers – Best Practices**

When adding the products to the page, it is best to create the first server according to the setup instructions in the download link on GitHub and then “duplicate product” for the rest of the servers that you are going to offer. This will minimize the time it takes to add the servers to WHMCS, as you will only have to make changes to the server specifications and pricing, rather than following all of the steps for each individual server.

You will notice that there are different default options for our `dedicated servers <https://www.limestonenetworks.com/dedicated-servers/bare-metal.html>`_ (i.e. some servers automatically come with 1TB SATA hard drives and some with 500GB hard drives, some with DDR3 RAM and some with DDR4 RAM). My recommendation is to group the similar configurations together to make the configurable options easier to assign. Also, if you prefer, you may deviate from our default packages and create your own (i.e. make all of your default packages include 1TB SATA hard drives or 16GB RAM).

**Cloud Servers – Best Practices**

When adding cloud servers as products, it is best to consider how you plan to display them on your site. The “cloud slider” is a popular interactive display, which allows your clients to choose between 3-6 different preconfigured cloud instances before making the next step to configurable options, where they can further customize the cloud server resources to their specific needs.

Initially, when adding the configurable options for cloud servers, adding all available configurable options to one configurable options list is recommended. Then duplicate the list for each different preconfigured server you are going to display and tick the boxes to hide each irrelevant option. Adjust the pricing for the remaining options accordingly (i.e. if your preconfigured server has 2 cores, 4GB RAM, & 60GB SSD drive, you would hide the options for 1 core, 2GB RAM, 40 GB SSD, etc. as they are irrelevant to this preconfigured server). Ultimately, this will be entirely up to you to customize.

**How the API interacts**


For dedicated servers, when an order is placed through your website, the API will not automatically provision the order, as dedicated servers are billed upfront on a monthly basis. So for that to work, you would have to have the full monthly payment available within your account balance in OnePortal.

When you receive the order, you will manually input it into our order form, at which time, you will be able to enter your promo code to receive your special discounted rate.

For cloud servers, which Limestone Networks bills hourly or monthly, when an order is placed through your site (assuming the plugin and configurable options are set according to the installation instructions in GitHub), our API will automatically provision the new server to your client through your account on an hourly billing basis. You must have at least $5.00 in your OnePortal account for this to take effect.

Once you notice that you have sold a new server, you are welcome to contact your account specialist or open a ticket to have the invoice converted to monthly billing.

For support, your company will act as the support agent to your clients. However, you may pass support requests to us on behalf of your clients. In OnePortal->Partner->OnePortal Lite (under the “Operational Customization” heading), you can configure how your clients reach your support when they are using OnePortal Lite. New clients will need to be added under the “My Clients” section in OnePortal->Partner->My Clients in order for them to have access to OnePortal Lite as the API does not collect any client information from WHMCS.
