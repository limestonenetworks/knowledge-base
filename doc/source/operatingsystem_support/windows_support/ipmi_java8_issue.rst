IPMI issues with Java 8
=======================

With the new Java 8 rolled out, it has been discovered that it can block access
to SuperMicro IPMI interfaces, if it doesn’t meet the minimum security
requirements.

Below are the steps that can be taken to fix this. This solution should work
for Windows 7 64bit, Windows 7 32bit, Windows 8 64bit, and Windows 8 32bit.
This fix may need to be implemented before each remote control session via a
SuperMicro IPMI.

- Go to the **Start Menu**
- Choose **Java**
- Click **Configure Java**
- You should be on the **General** tab
- Click **Settings…**
- Click **Delete Files…**

Make sure both “Trace and Log Files” and “Cached Applications and Applets” are
check marked and “Installed Applications and Applets” is unchecked.

- Press **OK**
- Click **Security**
- On this page, make sure that the Java security level is set to the **High**
  setting.
- Click **Edit Site List**, then add the IP address of the IPMI to the
  **Exception Site List….**
- Click **Apply**
- Press **OK** again on the General tab to exit
- Open the Remote Control session,  and you should then be able to use the
  IPMI.
