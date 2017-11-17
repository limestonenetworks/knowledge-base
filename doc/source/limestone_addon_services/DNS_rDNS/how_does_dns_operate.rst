How does DNS operate?
=====================

**How DNS operates / basic record management**


DNS stands for **Domain Name Service**. It is the system in which a domain name is converted into an IP address (in most cases). It all starts when you purchase a domain through a **registrar**, (Ex: `godaddy.com <https://www.godaddy.com/>`_).

As for the remainer of this article, we’ll call your domain “MYDOMAIN.COM”.

The primary role of a name-server is to handle requests, it accepts domain queries and returns a ‘record’. There are 2 most commonly used ‘records’, they are:

**- (A) Record** – This determines that IP Address of a domain, as an (Ex: When you enter a domain into your browser (Ex: Internet Explorer), your computer contacts a name-server, in which that name-server replied with an IP address of the domain you are trying to reach. Then your browser connects to that IP address.)

**- (MX) Record** – This determines which e-mail server handles e-mail for this domain. (Ex: You are sending an e-mail to support@limestonenetworks.com, the @limestonenetworks.com shows which domain the user **support** is at. The e-mail client will connect to your name-server and retrieve the ‘MX’ record, which is the Limestone Networks’ e-mail server.)

**Summary**

1. DNS stands for Domain Name Service.
2. The domain registrar determines which name-server handles request for a particular domain.
3. The basic operation of DNS is for the name-server to return information about a domain.
4. There are 2 most commonly used records.

**Using Limestone’s name-server(s)**

Please visit “How do I use Limestone’s DNS service?”

**Our Control Panel**

This section details how to create the most common records in our control panel.

**Creating an A Record in our Control Panel**

In order for your domain to resolve to your web server you will need to create an Address (A) Record for your domain in our control panel.

Under the DNS Tab in our control panel click on your domain, then click Add a Record. You will be creating two records. One so mydomain.com will resolve to your web server and another for www.mydomain.com For the first record leave the Host field blank, the Type: is Address (A), and then in the Address/Text field put your web server’s IP address. You can leave the TTL at its default. Now you will follow the same steps again except you will enter www in the Host field. Keep in mind the trailing . is already present after the field.


**Using your own name-server(s)**

In order to setup your own name-servers, such as:

- ns1.MYDOMAIN.com
- ns2.MYDOMAIN.com, etc

You’ll need to do the following:

- Setup DNS service on your server.
   - This can be a multitude of services, and the operating system can be nearly anything.. Linux, Windows, or Unix. Here are a few various programs for \*nix based operating systems:
      - BIND
      - DJBDNS

- Set your domain registrar’s name-servers to your nameservers and allow enough time to propogate:

  - ns1.MYDOMAIN.com
  - ns2.MYDOMAIN.com

- Modify your system records with domain records and allow enough time to take effect.
