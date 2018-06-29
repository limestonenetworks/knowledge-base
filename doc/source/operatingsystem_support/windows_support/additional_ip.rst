How do I set additional IPs in Windows?
=================================================

By default, Limestone only binds your first primary IP address. This is because
there are different methods of applying your additional IPs that may require
that they not be bound originally.

**Basic**

Here is the simplest way of binding your additional IPs:

1. Login to Remote Desktop
2. Go to Control Panel-> Network Connections -> Local Area Connection (make
   sure that the IP on this connection is not 10.*. If it is, use the other
   Local Area Connection)
3. Right-click on Properties
4. Select Internet Protocol (TCP/IP)
5. Click Properties
6. Click Advanced
7. Click Add and add the new IPs with the correct Subnet Mask

**Advanced**

If you are adding multiple IP addresses, you can also use the following in the
command prompt.

::

 FOR /L %I IN (x,1,y) DO netsh interface ip add address "Local Area Connection
 2" 216.245.218.%I 255.255.255.224

- x = The starting octet. This should be the one after your primary. (0.0.0.x)
- y = The ending octet. Your last available IP.

You will need to change “216.245.218.” and “255.255.255.224” to match your IPs
and subnet.

.. disqus::
