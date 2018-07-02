How can I tell if I’m being attacked?
=====================================

When experiencing a DoS or DDoS attack, the first thing you will most likely
notice is that your server is unresponsive or is very slow to respond.

**Check your Bandwidth Graphs**


The first thing you should do is check your server’s bandwidth graphs. You can
do this through our control panel by visiting your `Bandwidth Statistics
<https://one.limestonenetworks.com/servers/bandwidth.html?range=day>`_
page and viewing the past 24 hours or even the past hour alone. If you see that
your traffic has spiked and the port is fully saturated (or close to it), you
are most likely under attack.


Please note that the Enterprise DDoS Protected IP’s will not show in the
Security Center and the bandwidth stats will not show the attack unless the
protection is failing.

**Identify and Block Attackers**


If you have some connectivity to your server, you can attempt to block some of
the attack by blocking IP addresses having several connections to your server.
Use the following command to list your active connections by IP address:

::

 netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n

You can then use IP Tables, or the firewall of your choice, to block all
traffic from that IP address.

An IP Tables example would be:
::

 /sbin/iptables -I INPUT -s x.x.x.x -p tcp -j DROP
 /sbin/iptables -I INPUT -s x.x.x.x -p udp -j DROP

This would cause all TCP and UDP traffic to be dropped from this specific IP
address (represented by x.x.x.x).


**Helpful Articles on Blocking Attackers**


- `WHT – DDoS Deflate <http://www.webhostingtalk.com/showthread.php?t=877639>`_
   - (D)DoS Deflate is a lightweight bash shell script designed to assist in
     the process of blocking a denial of service attack. It utilizes the
     command below to create a list of IP addresses connected to the server,
     along with their total number of connections. It is one of the simplest
     and easiest to install solutions at the software level.


- `cyberciti.biz – tcptrack <https://www.cyberciti.biz/faq/rhel-track-monitor-tcp-connections-on-network/>`_
   - tcptrack is a sniffer which displays information about TCP connections it
     sees on a network interface. It passively watches for connections on the
     network interface, keeps track of their state and displays a list of
     connections in a manner similar to the unix ‘top’ command. It displays
     source and destination addresses and ports, connection state, idle time,
     and bandwidth usage.

**Notify Limestone**

If you have no connectivity to your server, or the blocks you have put into
place are not stopping the attack, open a ticket with our Support department.
We will do our best to mitigate the attack and restore connectivity to your
server quickly.

.. disqus::
