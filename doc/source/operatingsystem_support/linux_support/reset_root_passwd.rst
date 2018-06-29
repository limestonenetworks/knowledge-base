How can I reset my root password?
=================================


This article explains how to reset the root password if you no longer know it.
You will require KVM access to your server in order to perform these steps.


**CentOS/Fedora**

- Through the KVM, initiate a restart of your server by sending the shutdown
  command

::

 shutdown -r now

- When it comes to the **Loading CentOS/Fedora** Grub Bootloader screen hit
  **esc**.(Right after you get to the network boot screen it will be at the
  grub bootloader screen)

- At the grub screen select the default OS & hit **e** to edit.

- Then you should have 3 lines of text. Select the line that starts with
  **kernel** & ends in **root=label=/**

- Press **e** to edit the line, and at the end of the line add a space and then
  put a capital **S**.

- Then enter to save & go back to the previous screen.

- Then hit **b** for boot with that line selected.

- It will enter you in single user mode and you get a bash prompt.

- Then you can just type **passwd** enter new password and reboot.

You will not need to re-edit the grub loader it reverts to normal after the
next reboot.

**Debian**

Reboot and edit the Grub kernel line add a space then the following at the end
of the line. (like ‘Alternate Method’ above)
::

  init=/bin/sh

Then run this command to remount the root partition in read/write mode.
::

  mount -o remount,rw /

and reset the root password as normal with the **passwd** command.

.. disqus::
