Install Softaculous on a WHM Dedicated Server
=============================================

This guide will show you how to install Softaculous on a WHM dedicated server.

**Before the Installation**


- Obtain a licensed WHM server

- If you have a firewall, whitelist IPs to download and update Softaculous scripts

  - api.softaculous.com (IP : 216.18.221.243)
  - s1.softaculous.com (IP : 192.99.110.112)
  - s2.softaculous.com (IP : 76.164.222.115)
  - s3.softaculous.com (IP : 76.164.201.252)
  - s4.softaculous.com (IP : 138.201.24.83)
  - s7.softaculous.com (IP : 104.250.159.187

**Installing Softaculous**

Enable ionCube Loaders

- In WHM (as root user), navigate to Server Configuration -> Tweak Settings -> PHP
- Enable the loader by placing a check in the box next to “ioncube”
- Click ‘Save’

Once you have enabled the ionCube Loaders, SSH into your server and enter the following commands:
::

 wget -N http://files.softaculous.com/install.sh
 chmod 755 install.sh
 ./install.sh

Now visit your WHM web interface.

Navigate to Plugins -> Softaculous – Instant Installs.

If the installation was successful, you will see the home screen of Softaculous displaying the Software Info

**Installing with Proxy Settings**

If you need to install Softaculous using proxy settings then you can pass the parameters using the command below:
::

 wget -N http://files.softaculous.com/install.sh
 chmod 755 install.sh
 ./install.sh proxy proxy_ip=YOUR_IP:PORT proxy_auth=USERNAME:PASSWORD

Proxy Parameters:

- proxy_ip : Enter your Proxy server’s IP and port
- proxy_auth : Enter the proxy server’s authentication details (Username and Password)
