How do I set up SSH key authentication?
=======================================

SSH packets being sent from the SSH client to the server are encrypted with a
form of shared-key cryptography, using a random key which is generated for each
new connection and thrown away when that connection is over. The client and the
server use public-key cryptography to agree on the session key, and either
party may request a re-keying of the session at any time.

Once you become familiar with SSH keys, communication and file copying between
servers / clients will be secure, quicker, and more convenient.

Here’s an example on setting it up between a CentOS Client and CentOS Server:

On the client, do the following:

- Goto the .ssh directory, which is located under /root – full path is
  ``/root/.ssh``
- Now let’s create our private and public keys and put them into a file.

::

 ssh-keygen -t rsa

This created a 1024 bit key, and creates 2 files.

1. id_rsa – This holds your client’s ``PRIVATE`` Key.
2. id_rsa.pub – This holds your server’s ``PUBLIC`` key.

Now, let’s place the key ``id_rsa.pub`` into the servers authorized_keys file.
Located at: ``/root/.ssh/authorized_keys``, If this file is not already there,
we will create it.


Next you need to copy the key to your system. We’ll copy the key over via a
file copying program called rsync
::

 rsync -av -e ssh id_rsa.pub <SERVER_IP>:/root/.ssh/

Make sure to change ``SERVER_IP`` to the servers IP address.

After doing this command, you will be prompted for the root password of the
server, type it and press enter.

Now, on the server, do the following::

 cd /root/.ssh
 cat id_rsa.pub >> authorized_keys
 chmod 600 authorized_hosts

The 2nd command copies the contents of id_rsa.pub into authorized_keys file.

The 3rd command gives it the correct permissions to be run by the system.

Now, back on the client, do the following::

 cd /root/.ssh
 eval `ssh-agent`
 ssh-add id_rsa
 ssh-add -l

2nd command: Starts the SSH agent program.

3rd and 4th command: Adds your private key into memory.

Simply SSH into the server.
::

 ssh <server_IP>

When prompted, type in the root password. Now exit out and try to SSH into the
server from the client once more. This time – you shouldn’t be prompted for a
password.
