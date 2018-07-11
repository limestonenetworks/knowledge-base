=======================================
How do I install an OS through my IPMI?
=======================================

**IPMI Virtual Media**

**How To For Single CPU Xeons (X3400)**

1. Login to the IPMI interface by using https://[ip-address] in any browser.
You should have been provided the IP address of your IPMI interface in your
Welcome E-Mail or Provisioning Ticket. If you do not have this URL please
open a support ticket. The username and password is the same as your
control panel login.

.. image:: /image/Ipmi_login.png

2. After you login go to Remote Control > Console Redirection, and then click
Launch Console. This will launch a Java Console interface.

.. image:: /image/Ipmi_console.png

3. After a few seconds a toolbar should load in this Java window.
Click Virtual Media in the top left hand corner and then Virtual Storage.

.. image:: /image/Ipmi_vm.png

4. Go to the CDROM&ISO Tab and chose ISO File as the Logical Drive Type.
Then click Open Image and select the .iso file from your computer.
Once it has been selected click Plug in and click OK.
The ISO file should now be connected to the computer.

.. image:: /image/Ipmi_oi.png

**Setting The BIOS**

You will need to press F10 or F12 to enter the boot Menu and then Select
Boot from USB-CDROM. Setting it in the BIOS as your first boot device
will not work. The BIOS does not detect it, and skips over it initially.
Legacy USB Storage Detect MUST be enabled.

.. disqus::
