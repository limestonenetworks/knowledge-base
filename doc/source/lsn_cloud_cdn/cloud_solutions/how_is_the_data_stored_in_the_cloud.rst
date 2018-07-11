====================================
How is the data stored in the cloud?
====================================

The storage for the cloud is made up of a distributed SAN.
All of the SSD drives in the hypervisors are part of a striped and mirrored
RAID over a special storage network. Your instance is primarily stored
on the hypervisor that is serving it for quick access,
making our setup both Local and SAN.

.. disqus::
