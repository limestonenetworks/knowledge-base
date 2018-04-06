Hardening CentOS
================

**What will this script do?**

- Install useful packages such as tcpdump, mtr, zsh, perl and logrotate
- Setup automatic yum updates
- Set password policies
   - Passwords will expire every 180 days
   - Passwords may only be changed once a day

- Set OS policies
   - Set idle users to be disconnected after 15 minutes

- Install (if it is not installed) and configure IPTables firewall
   - Open specified TCP/UDP ports
   - Set rules to block common attacks
      - Syn Floods
      - Fragmented Packets
      - Malformed XMAS Packets
      - Drop NULL packets
      - Limit pings to 3 per second and bursts of 25
      - Discourage Port Scanning

   - Set up Connection Tracking

- Install DDoS Deflate
   - More information about DDoS Deflate is available at
     https://www.interserver.net/tips/kb/installing-configuring-linux-ddos-deflate/

- Install CHKROOTKIT
   - Scheduled to check daily for issues and email your Admin Email
   - More information about CHKROOTKIT is available at
       http://www.chkrootkit.org/

- Install rkhunter (Root Kit Hunter)
   - Scheduled to check daily for issues and email your Admin Email
   - More information about rkhunter is available at
     http://www.rootkit.nl/projects/rootkit_hunter.html

- Install LSM (Linux Socket Monitor)
   - Runs in the background and watches for changes in sockets

- Secure the SSH Daemon
   - Change the SSH port to a random number
   - Create an “admin” user
   - Make it so only the “admin” user can be logged into over SSH

**Downloading the Script**::

    cd /root
    wget http://mirror.lstn.net/scripts/hardening/centos.sh
    chmod +x centos.sh


**Modifying the Variables**::

    vim centos.sh

``You may customize TCPPORTS and UDPPORTS, however``
``the defaults in there now should cover most common processes.``


**Run the Script**::

    ./centos.sh

**What to do afterwards**

After it completes, you will get a message like::

    ******************************************
    YOUR SERVER IS NOW HARDENED
    ------------------------------------------
    SSH User: admin
    SSH Pass: 254457cb9448226
    SSH Port: 5575
    Admin Email: admin@fake.lstn.net
    ******************************************

    You must now reconnect to this server using the information above
    Changing the SSH port has caused this connection to freeze.
    BEFORE CLOSING THIS WINDOW please note your information above.
