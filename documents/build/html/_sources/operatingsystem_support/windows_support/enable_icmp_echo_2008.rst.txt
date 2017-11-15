How do I enable ICMP echos in Server 2008?
==========================================

To enable ICMP replies in Windows Server 2008 you must allow ICMP packets through the windows Firewall

1. Press Start
2. Goto -> Administrative tools
3. Click on ‘Windows Firewall with Advanced Security’
4. Click on ‘Inbound Rules’
5. Scroll down to find: ‘File and Printer Sharing (Echo Request – ICMPv4-In)’
6. Right-click on this and choose ‘Enable Rule’

Congrats, you can now ping the 2008 server.
