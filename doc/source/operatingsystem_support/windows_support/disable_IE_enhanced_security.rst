How do I disable Internet Explorer Enhanced Security?
=====================================================

For Windows 2003
^^^^^^^^^^^^^^^^

Windows Server 2003 is shipped with security locked down by default. Part of
this locking down is Internet Explorer Enhanced Security which is an extra
layer of protection when surfing the internet using Internet Explorer.

You can uninstall the entire Configuration, or just for users, or just for
Administrators.

The un-installer is set up like this::

 - Enhanced Security
    - For Administrators
    - For Users

If you have non-admin users connecting via Remote Desktop or Terminal Services,
you may wish to leave the Users configuration installed. This tutorial will
remove it for **all users**.

**Method:**

- Click Start, then Control Panel, and then select Add/Remove Programs

- Click Add/Remove Windows Components

A window will pop-up, click the check mark next to Internet Explorer Enhanced
Security Configuration (to ``uncheck`` it). If you’d like to only disable it
for Administrators or for Users only you can click “Details” and change this
setting individually.

Press Next, it will take a couple of seconds to finish, and then it’s all done!

For Windows 2008 it is a little different
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, open the Server Manager by going to Start > Server Manager

In the Server Manager browse to the Security Information section in the right
hand pane and click ‘Configure IE ESC’. IE ESC is located in the very lower
right-hand corner of the window.

In the Internet Explorer Enhanced Security Configuration window decide for whom
you want IE ESC enabled or disabled and click OK.

It can be enabled/disabled for Administrators only or for all users

For Windows 2012 it is almost like 2008
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the Windows Server 2012 server desktop, locate and start the Server Manager.

Select Local Server (The server you are currently on and the one that needs IE
Enhanced Security disabled)

On the right side of the Server Manager, you will find the IE Enhanced Security
Configuration Setting. (The default is On)

You have two settings that can be disabled, one only affects the Administrators
and the other all users. Make your selection to Off for Administrators, Users
or both.
