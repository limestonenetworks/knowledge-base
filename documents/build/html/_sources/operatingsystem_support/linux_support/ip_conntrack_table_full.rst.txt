Receiving an “ip_conntrack: table full” error.
==============================================

On OpenVZ/HyperVM machines sometimes the ip_conntrack table will become full and drop packets. You can tell if it is doing this by looking in your /var/log/messages file.

**To find out the current limit run**::

    sysctl net.ipv4.netfilter.ip_conntrack_max

Then to increase it edit::

    /etc/sysctl.conf

and change the line::

    net.ipv4.netfilter.ip_conntrack_max = to a higher number

Adding **5000** or **10000** to the current max should be fine.

Once you have saved the file, to reload the new configuration run::

    sysctl -p

You should be all set and the machine should not be dropping any packets.
