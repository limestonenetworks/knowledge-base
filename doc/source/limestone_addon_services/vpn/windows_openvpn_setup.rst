VPN Install On Windows 8.1
==========================

This howto will assist you with installing OpenVPN to access services on the
Limestone Private Network

For example, services available on the private network include: The `private
interfaces <http://limestonenetworks-knowledge-base.readthedocs.io/en/latest/limestone_addon_services/vpn/limestone_private_tunnel.html>`_
on your servers,
`Shared NAS Drives <http://limestonenetworks-knowledge-base.readthedocs.io/en/latest/limestone_addon_services/nas/setup_nas_acc.html>`_,
and
`IPMI devices <http://limestonenetworks-knowledge-base.readthedocs.io/en/latest/limestone_addon_services/kvmoip/access_server_ipmi.html>`_
for your servers.

1. Download and launch the OpenVPN installer for your OS from `OpenVPN’s
   website <https://openvpn.net/index.php/open-source/downloads.html>`_.

.. image:: /image/vpn001.png

.. image:: /image/vpn002.png

2. Click through the installer menus to install OpenVPN.

.. image:: /image/vpn003.png

3. Install the TAP driver when prompted.

.. image:: /image/vpn004.png

.. image:: /image/vpn005.png

________________________________________________________________________________

4. At this point OpenVPN is installed and **you should REBOOT before
continuing the installation process**. The reboot is necessary because we
typically do not see the tunnel network interface registered until a reboot
occurs.

5. Download the Limestone Private Network OpenVPN configuration files from your
`OnePortal account’s VPN page
<https://one.limestonenetworks.com/servers/vpn.html>`_.

.. image:: /image/vpn006.png

6. Copy the VPN configuration files from your downloads folder to
C:\Program Files\OpenVPN\config.

.. image:: /image/vpn007.png

.. image:: /image/vpn008.png

7. Approve the file copy operation.

.. image:: /image/vpn009.png

8. Right click the OpenVPN GUI shortcut on your desktop and access the
Properties menu.

.. image:: /image/vpn012.png

9. Select the Compatibility tab, and check “Run this program as an
administrator”. Then click OK.

.. image:: /image/vpn013.png

10. Launch the OpenVPN GUI app from the desktop shortcut, then find the OpenVPN
GUI icon in your taskbar. Right click it to display the installed Limestone
profiles, and connect to one.

.. image:: /image/vpn014.png


We recommend using the UDP profile for the best performance. A TCP profile is
also provided in case you are on a restrictive, firewalled network that will
not permit the UDP profile. The TCP profile is more reliable in these cases
however it will not be as fast as the UDP tunnel.

11. Use your OnePortal credentials to log in to the VPN.

.. image:: /image/vpn015.png

12. You are now connected to the VPN and can access IPMI cards and other
private network services.

.. image:: /image/vpn016.png

.. disqus::
