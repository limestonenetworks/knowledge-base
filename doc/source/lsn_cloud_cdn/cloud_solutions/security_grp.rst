Creating security groups for cloud VMs
======================================

**Security Groups** can be created and managed in the **“Access and Security”** tab of the control panel under the **“Security Groups”** tab.

 
.. image:: /image/securitygroups.png

Press the “Create Security Group” button to begin.
Give the group a name and description and press the “Create Security Group” button.
Once created you can create the rules for the group by pressing the “Manage Rules button” under the “Actions” tab.

.. image:: /image/rules.png

Here you can set rules for both IPv4 and IPv6 protocols.
To create a rule press the “Add Rule” button. 

.. image:: /image/addrule.png

- **Rule** Here you can choose the type of rule you would like to create.
- **Direction** Ingress is for all traffic incoming to the server. Egress is for all traffic coming from the server.
- **Open** Port allows you to choose whether this rule will be for a specific port or range of ports
- **Port** Input your port or range of ports here.
- **Remote** allows you to choose whether this rule will be for a set IP range (CIDR) or members of an existing security group (Security Group)
- **CIDR** Input the IP range that will be affected by this rule.

Press the **“Add”** button to create the rule.
