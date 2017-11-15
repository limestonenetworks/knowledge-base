How do I set up the local yum repo?
===================================

You may now get your CentOS installs and updates locally on Limestone’s network. When routed correctly, it will not count against your monthly bandwidth.

Yum Configuration
^^^^^^^^^^^^^^^^^

Edit the config::

 vi /etc/yum.repos.d/CentOS-Base.repo

And put the following::

 [base]
 name=CentOS-$releasever - Base
 baseurl=http://centos.mirror.cust.lstn.net/$releasever/os/$basearch/
 gpgcheck=1
 gpgkey=http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-5
  
 [update]
 name=CentOS-$releasever - Updates
 baseurl=http://centos.mirror.cust.lstn.net/$releasever/updates/$basearch/
 gpgcheck=1
 gpgkey=http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-5
 
 [addons]
 name=CentOS-$releasever - Addons
 baseurl=http://centos.mirror.cust.lstn.net/$releasever/addons/$basearch/
 gpgcheck=1
 gpgkey=http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-5

 [extras]
 name=CentOS-$releasever - Extras
 baseurl=http://centos.mirror.cust.lstn.net/$releasever/extras/$basearch/
 gpgcheck=1
 gpgkey=http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-5
 
 [centosplus]
 name=CentOS-$releasever - Plus
 baseurl=http://centos.mirror.cust.lstn.net/$releasever/centosplus/$basearch/
 gpgcheck=1
 gpgkey=http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-5

Correctly Route the Traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

 ip route add 10.0.0.0/8 via <strong>private-gateway-ip</strong> dev <strong>private-interface</strong>


If you want this to save after reboot, add to /etc/sysconfig/network-scripts/route-private-device

::
  
 10.0.0.0/8 dev <strong>private-interface</strong>

**Example**::

 10.0.0.0/8 dev eth1
