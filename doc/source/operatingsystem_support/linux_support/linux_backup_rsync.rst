==============================
How to Create Backups on Linux
==============================

There are various different methods to creating backups on Linux and also may be dependent on your distribution as well as your
preferences. Some of these include Tar, DD, Gnome Disk Utility, Acrois True Image, Norton Ghost for Linux, and CloneZilla to name a few.
However in this article, we will be using rsync as our example.

Please note that the majority of the information in this article was gathered from
`SpiceWorks <https://community.spiceworks.com/how_to/114945-centos-7-backup-and-restore>`_.
I have condensed or removed parts that were either to long, unnecessary, or irrelevant to just doing a backup. I have also put
additional examples and a few links to help with understanding
how some of the options work.

 **Install rysnc**

- **Redhat/CentOS**

 ::

      yum install rsync

- **Ubuntu**

 ::

      apt-get install rysnc

 **Running rsync one time backup**

 Here you will need to specify source, `option <https://www.computerhope.com/unix/rsync.htm>`_, and destination.

- Ex::

    rsync [OPTION] … SRC … [USER@]HOST:DEST
    rsync [OPTION] … [USER@]HOST:SRC [DEST]

 So in order to back up the entire system while excluding unneeded, you would run the following.
 /* being the source directory and all sub-directories and /home/user/backup being the destination.

 ::

    rsync -aAXv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/home/user/backup"} /*
    /home/user/backup

 **Automatic Backups**

 If you want to run backups automatically, the best way to do that would be to set this up through Cron job.

- Please note that if you want this to run automatically to a separate machine, you will need to configure SSH key pair so that a
password is not needed to be entered.

**Compress and move the files to another server**

 Compress using tar with the appropriate `options <https://www.tecmint.com/18-tar-command-examples-in-linux/>`_. You will want to put
 this into another directory so that tar does not include the .tar file in the archive.

 ::

    cd /home/user/backup
    tar zcvf /home/user/server-backup.tar ./

**Copy the .tar to another Linux machine using scp**

 ::

    scp /home/user/server-backup.tar
    user@ipaddress:/locationofdestination/server-backup.tar

 Alternatively you can also use an application such as `WinSCP <https://winscp.net/eng/download.php>`_ to download the file to your
 Windows desktop.

**Restore your Backup**

Once you have re-installed your OS has been reinstalled, you can copy the file back to the server and extract your files.

1. Copy your files to your server either using `WinSCP <https://winscp.net/eng/download.php>`_ or SCP. SCP ex. below.

 ::

    scp user@ipaddress:/locationofdestination/server-backup.tar /mnt

2. Extract the tar archive to /mnt with the appropriate `options <https://www.tecmint.com/18-tar-command-examples-in-linux/>`_.

 ::

    tar xvf /mnt/server-backup.tar

3. Create a /BOOT folder and mount /dev/sda1 to it and move files from /mnt/boot to /BOOT.

 ::

    mkdir /BOOT
    mount /dev/sda1 /BOOT
    mv /mnt/boot/* /BOOT/

4. Unmount /BOOT/

 ::

    umount /BOOT/

**Mount the required folders and chroot into /mnt**

 ::

    mount /dev/sda1 /mnt/boot/
    mount --bind /dev /mnt/dev
    mount --bind /sys /mnt/sys
    mount --bind /proc/ /mnt/proc
    chroot /mnt/

**Install grub**

- **Redhat/CentOS**

 ::

     grub2-install /dev/sda

- **Ubuntu**

 ::

    grub-install /dev/sda
    grub-update

**Updating fstab**
 After moving everything over, the UUID for the boot partition will need to be changed in fstab.

1. Find the new UUID with

 ::

    blkid /dev/sda1

 Ex Output:

 ::

    /dev/sda1: UUID="05221ad7-e319-4339-bb54-36b40f3b1b04" TYPE="xfs"

2. Open /etc/fstab with a text editor and comment out (#) out the old UUID then add your new UUID.

 Ex::

    /dev/mapper/centos-root / xfs defaults 1 1
    #UUID=49eb6416-2512-4129-a4be-f043c45561d5 /boot xfs defaults 1 2
    /dev/mapper/centos-swap swap swap defaults 0 0
    UUID=05221ad7-e319-4339-bb54-36b40f3b1b04 /boot xfs defaults 1 2

**Regenerate grub config file**

 ::

    grub2-mkconfig -o /boot/grub2/grub.cfg

**Exit chroot and unmount the folders**

 ::

    exit
    umount /mnt/dev/
    umount /mnt/sys/
    umount /mnt/proc/
    umount /mnt/boot/

**Network interface and MAC address**

- **Redhat/CentOS**

 Your interface and MAC address so you will need to reconfigure your network config file. Using either ip addr or ifconfig -a you should
 find the correct network adapter name as well as the mac address.

 ::

    [root@test ~]# ifconfig -a
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 162.253.43.58  netmask 255.255.255.0  broadcast 162.253.43.255
        inet6 2607:ff68:100:a::a0  prefixlen 128  scopeid 0x0<global>
        inet6 fe80::f816:3eff:fe89:5069  prefixlen 64  scopeid 0x20<link>
        ether fa:16:3e:89:50:69  txqueuelen 1000  (Ethernet)
        RX packets 10756  bytes 12185686 (11.6 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10015  bytes 603201 (589.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

 Once you get the correct MAC and network name, you can edit your config file accordingly. I typically just remove the MAC address all
 together as it isn't required and just change the device name in the config file.

 Here we see the configuration file is named eth0

 ::

    cd /etc/sysconfig/network-scripts/
    [root@test network-scripts]# ls
    ifcfg-eth0       ifdown-post      ifup-bnep   ifup-routes
    ifcfg-eth0-ipv6  ifdown-ppp       ifup-eth    ifup-sit
    ifcfg-lo         ifdown-routes    ifup-ippp   ifup-Team
    ifdown           ifdown-sit       ifup-ipv6   ifup-TeamPort
    ifdown-bnep      ifdown-Team      ifup-isdn   ifup-tunnel
    ifdown-eth       ifdown-TeamPort  ifup-plip   ifup-wireless
    ifdown-ippp      ifdown-tunnel    ifup-plusb  init.ipv6-global
    ifdown-ipv6      ifup             ifup-post   network-functions
    ifdown-isdn      ifup-aliases     ifup-ppp    network-functions-ipv6

 You'll want to open the config file in a text editor (i.e. vi, vim, nano), change the MAC address to the new one or remove it
 completely. Below I have commented(#) it out as this disables it. You will also want to change the DEVICE name accordingly.

 ::

    [root@test network-scripts]#nano ifcfg-eth0
    BOOTPROTO=static
    DEVICE=eth0
    #HWADDR=fa:16:3e:89:50:69
    ONBOOT=yes
    TYPE=Ethernet
    IPADDR=192.168.90.3
    NETMASK=255.255.255.252
    GATEWAY=192.168.92.2
    DNS1=208.115.254.242
    DNS2=208.115.254.250

 If you want to go back to using eth0 modify the /etc/default/grub file and include

 ::

    net.ifnames=0

 at the end of

 ::

    GRUB_CMDLINE_LINUX=

 After that run

 ::

    grub2-mkconfig -o /boot/grub2/grub.cfg
    reboot

- **Ubuntu**

 On Ubuntu your network config will also likely need to be modified to work correctly. Use the following to find the following network
 devices and configure accordingly.

 ::

    sudo lshw -C network

 Then modify the hardware address in

 ::

    /etc/udev/rules.d/70-persistent-net.rules

 If that doesn't help modify grub to include this at the end

 ::

    biosdevname=0

 at the end of

 ::

    GRUB_CMDLINE_LINUX=

 After that run

 ::

    grub-update
    reboot

**Sources:**

 https://community.spiceworks.com/how_to/114945-centos-7-backup-and-restore

 https://en.wikipedia.org/wiki/Rsync

 https://www.maketecheasier.com/back-up-entire-hard-drive-linux/

 https://www.computerhope.com/unix/rsync.htm

 https://www.tecmint.com/18-tar-command-examples-in-linux/

 https://www.cubebackup.com/blog/automatic-backup-linux-using-rsync-crontab/


.. disqus::
