How Do I Remove My IP From Trend Micro’s DUL
============================================

If you encounter issues sending e-mail due to a listing in Trend Micro’s DUL
(Dial-up/Dynamic User List) the steps outlined below will walk you through how
to get your IP removed.

Trend Micro will list IP addresses in their DUL if they do not meet their
requirements. In order to have your IP(s) removed you need to change your rDNS
in our control panel and e-mail `Trend Micro’s DUL Team <dul@mail-abuse.org>`_.

Please `confirm your IP is listed <https://www.ers.trendmicro.com/reputations/index>`_
in the DUL before contacting Trend Micro.Below are Trend Micro’s
recommendations regarding delisting.

::

 At this time, your rDNS looks like this, which looks dynamic.
 This is what we call a generic naming convention:

 192.168.0.1 (1-0-168-192.reverse.lstn.net)

 If this IP is indeed static, then the rDNS needs to resolve to static.
 Here is 2 ways to do that.

 1) Add the word "static" to the rDNS to reference static. For
 example:
 1-0-168-192.static.reverse.lstn.net

 2) Change the rDNS to announce your server, for example:
 mail.domain.com (this is preferable if this is your mail server)

 Here are the naming conventions that we use to decide if an IP or
 CIDR is static or dynamic.
 Typical static rDNS terms:
 bus, biz, colo, ded, fix, mta, perm, server, smtp, static, wsip.

 Typical dynamic rDNS terms:
 adsl, cable, dhcp, dialup, dsl, dyn, home, isdn, modem, pool, ppp, or res.

Trend Micro must see these changes prior to any removals. Once you have changed
your rDNS email dul@mail-abuse.org stating that you have changed your rDNS to
reference its static assignment and are requesting removal. An example e-mail
is below.

::

 To: dul@mail-abuse.org
 Subject: DUL Removal for 192.168.0.1
 Body: The RDNS for 192.168.0.1 has been changed to reference that it is a static IP address.
 I would like to request removal of this IP from the DUL.

If you have any questions or issues regarding these steps please open a `support ticket
<https://one.limestonenetworks.com/support/newticket.html>`_.
