How do I connect to my other servers using the private interface?
=================================================================

**Limestone Private Tunnel**

Limestone keeps you connected in two different ways. Every server has two Ethernet cards in it. The first links the server to the outside world via our internet carriers. The second Ethernet card links the server into a back-end router we have on our network, a LAN type of setup.

The advantage is that if a customer has more than one server, using one as, say, a database server and the other as a traditional web server, they can transfer information between the two servers without sending any information out over the net. This configuration offers our clients a secure back-end network over which they can transfer and communicate between servers without wasting any of their bandwidth and without risking exposure of sensitive data to the Internet.

When traffic is configured correctly, this traffic is un-metered and doesn’t cost you any money. If you need assistance with this configuration, please open a support ticket.

**Please note:**

In order for your server to communicate with the Limestone Private Tunnel, it needs to be configured with static network routes.

For CentOS-based servers provisioned recently, we automatically add the correct routes to a file called /etc/sysconfig/network-scripts/route-ethX (where ethX is the private interface). If you have CentOS and the routes are not working correctly, please open a `support ticket <https://rw.limestonenetworks.com/support/newticket.html>`_.

Also keep in mind, if your route table is filled with extraneous routes, especially if any of them have anything to do with your private interface or the 10.x.x.x network, this may cause issues. For this reason, if you plan to utilize your own private network (either for VPSes or anything else), try to utilize either the 172.16.0.0/12 range, or the 192.168.0.0/16 range.

More information is available about private IP address ranges `here <https://en.wikipedia.org/wiki/Private_network#Reserved_private_IPv4_address_space>`_.

**Making it work**

**Windows**
::

 route -p ADD 10.0.0.0 MASK 255.0.0.0 [privategateway]

Replace [privategateway] with the gateway from your private block of IPs.

For example: if your private block is 10.5.21.108/30, then your gateway will be 10.5.21.109, and your usable IP (the IP you’ll use to actually contact the server) is 10.5.21.110.

Ex:  route -p ADD 10.0.0.0 MASK 255.0.0.0 10.5.21.109

**Linux**
::

 ip route add 10.0.0.0/8 via [privategateway]

or, sometimes a Linux system won’t have the ‘iproute2’ package, so use:
::

 route add -net 10.0.0.0 netmask 255.0.0.0 dev [privateifc]

Replace [privategateway] with the gateway from your private block of IPs.


For example: if your private block is 10.5.21.108/30, then your gateway will be 10.5.21.109, and your usable IP (the IP you’ll use to actually contact the server) is 10.5.21.110.

Replace [privateifc] with the network interface in your system that contains your private IPs.

To find which interface is your private, type the following command in Linux:
::

 route | grep -v "74.63" | grep -v "69.162" | grep -v "216.245" | grep -m 1 "255.255" | awk '{ print $8 }'

It will usually return either “eth0” or “eth1”. This will be your private interface.

**Please note:** Static routes created in this manner are not permanent and will be lost after reboot. To make the route persistent please see this article under the heading “`Linux Persistence Routes <https://www.cyberciti.biz/tips/configuring-static-routes-in-debian-or-red-hat-linux-systems.html>`_
“.
