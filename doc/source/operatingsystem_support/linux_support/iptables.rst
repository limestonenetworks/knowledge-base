How do I use iptables?
======================
**Warning**


Modifying rules on your server can cause the server to become inaccessible on
port 22 (SSH) or your alternate SSH port.

**Description / Basic Overview**

Everyone in the IT industry is very concerned with security, especially if
you’re a linux administrator. Many linux distributions come with several
services that you may not use or ever need but they’re running on your server
anyway. This can cause many security threats. With the slightest knowledge of
Linux firewalls (iptables) you can secure your linux server very quickly and
efficiently. In this article, I will either introduce you into iptables for
your first time, or help you become more efficient with iptables if you’ve
worked with them in the past.

As network packets flow in and out of the network interface card, they are
intercepted, analyzed and manipulated as ruled through the Linux firewall. As
the packet flows through the firewall rules and it reaches a rule that is
matches, it stops there and doesn’t continue through the rest of the rule set.
For instance, if there is a rule to drop all packets coming in through port 25
and then a rule directly after that says “accept 192.168.1.25 on port 25” That
packet will be dropped once it hits the first rule. It won’t even know there is
a second rule. Read the first example further down this article. There is an
example. There have been 3 main linux firewalls widely used, and they are as
follows:

**History**

- Ipfwadm which was merged into Linux 2.0. It can filter TCP, UDP, and ICMP
  packets only. It also does not support QoS. You can “insert” and “remove”
  rules. This doesn’t make it the most user friendly linux firewall on the
  planet.
- Ipchains which was merged into Linux 2.2. It supports QoS, Is very flexible
  with the configuration, as it has “replace” along with “insert” and “remove”.
  This makes ipchains more user friendly. Ipchains also has the ability to
  filter any IP protocol explicitly, not just TCP, UDP, and ICMP.
- Iptables. This iptables project was begun in 1998 by Rusty Russell. This was
  merged into Linux 2.3 in 2000, and is still widely used today. It supports
  stateful IPv4, and IPv6 protocol tracking and IPv4 application tracking. Has
  built-in PORTFW functionality. It is also very user friendly, as you’ll soon
  find out.

**Getting started**

Let’s take a look at our iptables list, see what is currently under there!
::

 /sbin/iptables -L -n

That will show you your complete iptables rule list, with as much information
as possible about each rule. Let’s break down what you’re looking at you should
see something similar to: (note: the following is an empty table you may have
some rules in yours).
::

 Chain INPUT (policy ACCEPT)
 target     	prot 		opt 		source               destination

 Chain FORWARD (policy ACCEPT)
 target     	prot 		opt 		source               destination

 Chain OUTPUT (policy ACCEPT)
 target     	prot 		opt 		source               destination

Flushing your list of rules can be good if you would like to rewrite your rules
completely as I’ve done plenty of times in the past. You can “flush” every rule
under iptables by doing
::

/sbin/iptables -F

However you may want to only flush all the rules under the INPUT, FORWARD or
OUTPUT chain. You can specify which chain to flush by either of the following:

- /sbin/iptables -F INPUT
- /sbin/iptables -F FORWARD
- /sbin/iptables -F OUTPUT

Additionally, you can save your rules so that when you restart your linux
server, the current rules will become active once again. You can save by doing
::

 /etc/init.d/iptables save

If you would wish for iptables to STOP running, you can initiate the following
command
::

 #> /etc/init.d/iptables stop

 Flushing firewall rules:                                   	[  OK  ]
 Setting chains to policy ACCEPT: filter                    [  OK  ]
 Unloading iptables modules:                                	[  OK  ]
 Of course, you can START iptables by doing
 /etc/init.d/iptables start
 Applying iptables firewall rules: 			[  OK  ]

As for an example, I have one below:

**Example**


You want to simply deny every IP address a connection to your SMTP server (tcp
port 25) except for the IP: 192.168.1.25.

The two commands for this are as follows
::

 /sbin/iptables -I INPUT -p tcp --dport 25 -j DROP
 /sbin/iptables -I INPUT -s 192.168.1.25 -p tcp --dport 25 -j ACCEPT

The reason I put the “DROP” command in before the “ACCEPT” is because a rule is
entered into the database, and then a rule that is added next is added directly
above the last one entered. Putting the DROP command before the ACCEPT let’s
the ACCEPT rule be read before the DROP command. Let’s break the rest of these
commands down:

**The first command:**

- ``-I`` is to insert the rule into the top of the chain. You would use -A to
  insert it at the bottom of the chain. (Note: you can do “–D” instead to
  delete the rule from the chain as well.)

- ``INPUT`` is the chain name. Input is the chain that is followed by
  “incoming” packets.

- ``-p`` is the protocol argument, you specify the protocol type with this
  command, notice the “tcp” after the “-p”

- ``–ddport`` is what specifies which port to filter. In this case it is 25,
  because that is what port SMTP runs on (by default).

- ``-j`` is the argument that specifies what to do with the packet. In this
  case, it’s going to be “DROPPED”

**The second command:**

The only difference between this command and the first one, is there is a (-s)
“src” IP address specified and the –j argument is “ACCEPT”.

Since a (-s) “src” address was not specified in the first argument, it assumed
that every address is to be dropped.

Ok, let’s save our current work.
::

 #> /etc/init.d/iptables save
 /sbin/iptables -L -n
 Chain INPUT (policy ACCEPT)
 target     prot opt source               destination
 ACCEPT     	 tcp  --  192.168.1.25         0.0.0.0/0           tcp dpt:25
 DROP      	 tcp  --  0.0.0.0/0                0.0.0.0/0           tcp dpt:25

Notice: how the “ACCEPT” rule is above the “DROP” rule.

.. disqus::
