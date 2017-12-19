How do I access my server’s IPMI?
=================================

All E3- and E5-based dedicated servers offered by Limestone Networks come with a built in IPMI. This device allows you console-level remote access and control of your server, as well as monitor system hardware and keep up with system alerts.


Before attempting to access your IPMI, you will need to configure and log in to the Limestone Private Network via your VPN. You may find a tutorial on install, configuration, and access here. Please note that you will not be able to access your IPMI unless you are actively connected to the Limestone Private Network via IPMI – this is for your security and to prevent unauthorized IPMI access from the outside world.


To access your IPMI, enter the One Portal control panel and navigate to the Services -> Service Packages page. From there, select the Tools dropdown for the server that you wish to utilize the IPMI of, and choose Launch KVMoIP.

.. image:: /image/kvm_image1.png

Once you have clicked this option, you will be taken to a login page for your IPMI. You simply log in using the same credentials that you use to log into One Portal, but please be aware that passwords in excess of 16 characters will cause issues with the IPMI and will not be able to log in. If this is the case, you will need to change your password via One Portal, fully log out of all Limestone Networks-affiliated pages, and wait 5 minutes for the change to propagate through our systems.

.. image:: /image/kvm_image2.png

Once you have logged into the IPMI, to take remote control of the server, choose Remote Control -> Console Redirection (on older models) or Remote Control -> Remote Console (on newer models). This will download a .jnlp applet launcher – you will need to have the latest Java Runtimes installed, and the IPMI will prompt you for this if this is not detected.

.. image:: /image/kvm_image3.png

.. image:: /image/kvm_image4.png

Once you have downloaded and launched the .jnlp file, you are now connected to your server’s IPMI KVM over IP remote console. You have full mouse and keyboard access to the server, as if you were physically right next to it.

Please be aware that due to the way that Supermicro deploys self-signed certificates for IPMIs, you may need to acknowledge an “unsafe” connection in your web browser and/or through Java. As this is being routed through our secure VPN and the Limestone Private Network, you can be confident that your connection and data is safe and secure.
If you are unable to access your IPMI for any reason, or attempts to launch the .jnlp file return with “Connection Failed”, please open a support ticket with as much information as possible and we will be glad to assist you.
