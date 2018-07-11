=========================
Malicious Network Traffic
=========================

**Why am I receiving this notification?**

An abuse ticket will automatically be opened on your account when
Limestone Networks has received an abuse report for an IP address
currently assigned to your server.

**What is Malicious Network Traffic?**

Limestone Networks considers Malicious Network Traffic as any of
the following:

**Port Scanning**

An attack that sends client requests to a range of server port
addresses on a host, with the goal of finding an active port and
exploiting a known vulnerability of that service.

**Malicious HTTP GET/POST requests**

An attack against a web server to discover commonly used scripts or
software, with the goal of exploiting a known vulnerability in that
software.

**Any type of unauthorized brute-force attack against another server**

An attack used for trying many combinations of standard or frequently
used username and passwords (e.g.: root/password).
These attacks are commonly directed towards SSH and RDP services.

**Why is my server sending out malicious network traffic?**

This type of activity typically occurs because a malicious script or
program was installed on the server. This may have been due to a compromise
of the server’s security or by a user granted access to your server.

**Common Attack Vectors**

- Login credentials have been brute forced or compromised
- User visited a malicious website and malware was installed without
  their knowledge
- A vulnerability in website software allowed the attacker to upload a
  malicious script
- A user knowingly installed malicious scripts/software on the server.

**How can I identify the script or software responsible?**

If your operating system is Linux we suggest using the “ps” command to
view the running processes on the system.

`How to show all running processes in Linux <https://www.cyberciti.biz/faq/show-all-running-processes-in-linux/>`_


If your operating system is Windows we suggest downloading and running
Process Explorer from Microsoft. Process Explorer is a more advanced version
of Windows Task Manager. You can use this program to help identify processes
running on your system that you do not recognize. You can also find where on
your system a process is running from and what connections to the internet it
is making.

`Download Process Explorer <https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer>`_


Resources:

`http://en.wikipedia.org/wiki/Port_scanner <https://en.wikipedia.org/wiki/Port_scanner>`_
`http://en.wikipedia.org/wiki/Brute-force_attack <https://en.wikipedia.org/wiki/Brute-force_attack>`_
`http://la-samhna.de/library/brutessh.html <https://www.la-samhna.de/library/brutessh.html>`_
