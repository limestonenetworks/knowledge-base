================================
How do I bind my additional IPs?
================================

**These instructions are for CentOS / Fedora specifically.**
By default, Limestone only binds your first primary IP address.
This is because there are different methods of applying your
additional IPs that may require that they not be bound originally.

Here is the simplest way of binding your additional IPs:

1) Find out which interface is your public

``[root@LSN-D#### ~]# route | grep -v "10." | grep -m 1 "255.255"
| awk '{ print $8 }'``

``eth1``

This shows that my public interface (does not have a “10.” address)
is ``eth1``.

**2) Create the route file**

Before running the command below, change ``“eth1”`` to your public
interface from step 1 and set your START and END IP addresses
in the range.

**Note:**
Your IPADDR_START should be your second usable IP as your primary
is already bound. The IPADDR_END value is your last usable IP.
If you are unsure what these values are
please check your welcome e-mail or open a `support ticket <https://rw.limestonenetworks.com/support/newticket.html>`_.

  ``echo "IPADDR_START=123.123.123.4``
  ``IPADDR_END=123.123.123.5``
  ``CLONENUM_START=0" >> /etc/sysconfig/network-scripts/ifcfg-eth1-range0``

**3) Restart your network interface**

  ``service network restart``

.. disqus::
