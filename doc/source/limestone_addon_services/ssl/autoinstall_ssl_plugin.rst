AutoInstall SSL Plugin Installation for cPanel
==============================================

1. Download the plugin from `here <http://mirror.lstn.net/limestone-
   sslstore/cPanel_AutoInstallSSL_latest.zip>`_
2. Copy the **autoinstallssl** folder from the zip file to your WHM/cPanel server, it requires 
   no specific location.
3. As the root user, run the install command at the prompt:

::

 cd autoinstallssl
 chmod 777 install
 ./install

4. Activate ionCube loaders from WHM panel.
   Go to “Tweak Settings “ menu under “Server Configuration “
   Click on PHP tab.
   Check the ionCube option and click on save.
5. Complete the `AUTO-UPDATE <http://limestonenetworks-knowledge-base.readthedocs.io/en/latest/limestone_addon_services/ssl/autoinstall_ssl_cpanel_auto_update_guide.html>`_ setup to ensure functionality in future versions
