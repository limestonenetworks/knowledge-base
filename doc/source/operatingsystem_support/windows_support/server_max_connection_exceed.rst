Terminal Server Has Exceeded Max Connections
============================================

This problem happens because Windows only allows two remote terminal services
connections to be logged in as an Administrator, and you’ve either got two
people already on that server as an Administrator, or more likely, you’ve got a
disconnected session that is still logged in (simply closing the RDP session
does not log you out, you need to log out from the Start Menu on the remote
server).

To force yourself to login as an admin (provided you have admin credentials to
log on with) execute the following from your local computer:

For users with XP SP3, Vista, or terminal services client => 6.1:

- Start > Run >

::

 mstsc /v:0.0.0.0 /f /admin

Otherwise:

- Start > Run >

::

 mstsc /v:0.0.0.0 /f /console

…Replace the 0.0.0.0 with your IP address, type in your username/password at
the prompt and you are good to go.

For more information on the mstsc command click `here <https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/ts_cmd_mstsc.mspx?mfr=true>`_.

Free bonus: Need to Ctl + Alt + Del in a RDP window? Don’t work? Try Ctl + Alt
+ End instead.

.. disqus::
