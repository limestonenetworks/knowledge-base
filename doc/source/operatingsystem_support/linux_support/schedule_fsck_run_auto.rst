How do I schedule FSCK to run automatically?
============================================

**Using cron to schedule an FSCK**

- By default, a fsck is forced after 30 reboots or 180 days.
- To avoid issues such as this, we recommend scheduling fsck to run a basic
  weekly check on your server to identify and flag errors.
  - Doing so can prevent unwanted, forced fsck from running in situations such
  as this one.
  - You can then, plan for a time at which a full system fsck is run.

For more info on running fsck please click `here
<https://en.wikipedia.org/wiki/Fsck>`_
For more info on scheduling tasks under Linux click `check
<https://en.wikipedia.org/wiki/Cron>`_

The following example syntax will add a weekly scheduled **scan-only** fsck and
output the results to a log file for review.
::


 crontab -e

enter the following text substituting *partition* with your root partition.

::


 @weekly fsck -nv /dev/*partition* > /var/log/weekly_fsck

When saving, do not change the existing file name.


**PLEASE NOTE–**

``This does not eliminate the need for a fsck.``
``You will still need to schedule a manual fsck.``

**To Force a fsck using shutdown command**
::


 shutdown -rF now

Bypass a fsck using shutdown command
::


 shutdown -rf now

``Note: Capital F will Force a FSCK, lowercase f skips a FSCK.``

FSCK will sometimes require the root password be entered on the console in
order to repair some issues with the filesystem, contact our support department
if your server does not respond after a reboot.
