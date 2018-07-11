===============================================
Drives not appearing in Windows 2008 installer.
===============================================

On Windows 2008 R2 64-bit systems, the Setup program tries to load Inbox
storage drivers first, by default. As a result, you must load the driver
for Adaptec Series 6/6Q/6E/6T controllers TWICE.

The first time you load the driver, the OS displays the message
“No drives were found’. Select ‘Load Driver’ again, uncheck
“Hide drivers that are not compatible…’, then select the Series 6
controller driver. On the second attempt, the driver will load successfully.

.. disqus::
