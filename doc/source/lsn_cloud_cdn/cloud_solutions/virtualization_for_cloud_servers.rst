What type of virtualization is used for cloud servers?
======================================================

There are a few main virtualization types: KVM, VMWare, OpenVZ and Xen. Out of
them, we chose KVM because it has been proven to be the fastest. This is mostly
due to how highly integrated it is with the hypervisor’s kernel.

Nested KVM
==========
Nested KVM is not supported at this time. It is still a young concept and we
will continue to watch for it to be production ready. You can however purchase
Citrix XenServer and run Xen within our cloud.

.. disqus::
