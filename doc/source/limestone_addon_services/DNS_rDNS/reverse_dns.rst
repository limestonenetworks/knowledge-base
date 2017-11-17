What is rDNS?
=============


rDNS is Reverse DNS.

rDNS operates in the exact opposite direction of DNS, it converts IP addresses into domains.

**What do we need rDNS for?**

One great use of rDNS is for e-mail servers. Example:

- Your e-mail server mail.yourdomain.com contacts mydomain.com’s mail server.
- mydomain.com resolves mail.yourdomain.com into 172.22.0.1, in order to send information back to the server.
- However, mydomain.com has security measures.. It wants to make sure 172.22.0.1 really is mail.yourdomain.com, so it performs a rDNS lookup.
- 172.22.0.1 turns out to resolve to mail.yourdomain.com, so it sends it’s data.

**How do I modify rDNS records for my IP(s)?**


The control panel enables the customer to modify rDNS entries directly to their IP address(s), via http://one.limestonenetworks.com/dns/reversedns.html.
