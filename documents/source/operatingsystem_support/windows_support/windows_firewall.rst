How do I block a specific IP from my server?
============================================

**windows Firewall**

First, you will need to open the IPSec snap-in:

1. Start -> Run -> mmc
2. File -> Add/Remove Snap-in…
3. Add…
4. IP Security Policy Management (Not to be confused with IP Security Monitor)
5. Local Computer

Highlight **Security Policies on Local Computer**

1. In the right pane, right-click and choose **Create IP Security Policy…**
2. This will start the IP Security Policy Wizard.
3. Choose **Next** Enter a **Name:** and **Description:**
4. UN-CHECK **Activate the default response rule.** Leave **Edit properties** checked
5. and click **Finish**

Under **Rules** choose **Add…** This will start the Security Rule Wizard.

1. Hit **Next**
2. This rule does not specify a tunnel.
3. Local area networks (LAN)
4. This will open the **IP Filter List**
5. Choose **Add…**
6. Enter a **Name:** and **Description:** *Use the IP as the name for identification purposes.*
7. Choose **Add…**
8. **Next**
9. **Description:** is optional here, though I’d put the IP to block again…
10. UN-CHECK **Mirrored. match packets with the exact opposite source and destination address.**
11. For **Source address:** Use the Drop-down to choose **A specific IP Address** and enter the IP address to IP to be blocked.
12. **Next**
13. For **Destination address:** Use the Drop-down to choose **My IP Address**
14. **Next**
15. For **Select a protocol type:** leave the drop-down on *Any*
16. **Next**
17. Make sure **Edit properties** is unchecked and Click **Finish**

This will return you to the **IP Filter List** press **O** to close it.

1. You will now see and should select the radial for the filter list you just created.
2. **Next**
3. This will open **Filter Action**
4. Choose **Add…**
5. **Next**
6. Enter a **Name:** and **Description:** This action is simply for blocking traffic so name it **BLOCK**
7. **Next**
8. Select the **Block** radial
9. **Next**
10. Make sure ‘Edit properties’ is unchecked and Click **Finish**

This will return you to the **Filter Action** selection You will now see and should select the radial for the filter action you just created. Make sure ‘Edit properties’ is unchecked and Click ‘Finish’

Click **OK** to close the Policy you’ve just created.

The new policy should now show up in the right pane… to activate it, simply right-click and choose **assign**

More information can be found in this downloadable guide from Microsoft: `here <https://www.microsoft.com/en-us/download/details.aspx?id=11698>`_
