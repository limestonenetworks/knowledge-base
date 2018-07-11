==========================
How do I run a traceroute?
==========================

Both Windows and Linux have the ability of diagnosing the health
of a connection between a source and destination machine by also
testing the communication status of the devices that make the
connection possible.

Windows uses the command **tracert** for this utility.
Linux uses the command **traceroute** for this utility.

The route is determined by examining the ICMP Time Exceeded
messages sent back by intermediate routers. Note that some routers
silently drop packets with expired TTLs and are invisible to
TRACERT / Traceroute utilities.

**How to run a traceroute**

**Windows**

- Open a command prompt by going to Start->run->type command->press enter.
- Type the command: tracert

For example:

 ``C:\>tracert 4.2.2.2``

**Linux**

For linux the command would be:

 ``traceroute <ip address>``

For example:

 ``traceroute 4.2.2.2``

.. disqus::
