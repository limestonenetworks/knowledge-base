=======================================================
Large file transfer gives error: Corrupted MAC on input
=======================================================

**Symptom**

When you transfer a large file by HTTP it will disconnect and
give you this error:


``Disconnecting: Corrupted MAC on input.``

This can also happen on SSH, FTP or other protocols as this is a
bug with the kernel driver for the network.

**Solution**

Turn off “offload check summing” with the following command:



``ethtool -K eth0 rx off tx off``

Depending on the Ethernet driver in use this may not work as some
drivers do not support turning off this feature.

.. disqus::
