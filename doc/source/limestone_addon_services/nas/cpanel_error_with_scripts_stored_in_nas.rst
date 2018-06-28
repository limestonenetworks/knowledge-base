cPanel errors with scripts stored on NAS
========================================

When using a cron script executed by cPanel that is stored on the Limestone
NAS, you will need to modify the mount command to include the uid and gid of
the cPanel user which is running the bash script.

For example:
::

 mount -t cifs -o username=cli\
  ####,password=yourPassword,uid=yourCpanelUid,gid=yourCpanelGid, \
 file_mode=0755,dir_mode=0755 //74.63.205.205/nas.nas.cli
  #### /mnt/nasCpanelUser

For more information about Limestone’s NAS, please visit our articles
`Limestone Networks NAS
<http://limestonenetworks-knowledge-base.readthedocs.io/en/latest/limestone_addon_services/nas.html>`_.
