====================
How do I run a ping?
====================

PING stands for Packet INternet Groper.

This is a simple diagnostic tool implemented in both Windows and Linux
that enables you the ability to test for basic communication between two
network nodes within a LAN or across the WAN/Internet.

The concept is simple – a special packet is sent from a source machine
to a destination the machine at which the destination machine
responds back.

The time it takes for this process to complete helps determine
two things:

  - Does the destination machine respond?
  - How long does it take the destination machine to respond back?

To run this tool is very simple.

For windows you simply open a command prompt:

  ``Go to Start->run->type CMD->press enter``

Within the command prompt you will type:

  ``ping destination-IP -n 10``

For example:

  ``ping 4.2.2.2 -n 10``

.. disqus::
