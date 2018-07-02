How do I configure Exim for better logging?
===========================================

**What will these instructions do?**


What this addition does is it adds valuable logging information to your
exim_mainlog file so that you can determine where messages are coming from,
whos sending the message and from what directory on your server the user NOBODY
is originating from, if your seeing mail leaving as nobody. In addition, it
adds very useful information to exim_mainlog to help you decipher email coming
and going.

**Here is an example**

::

 2003-06-27 14:06:18 cwd=/home/usersite/public_html/forums 3 args:
                     /usr/sbin/sendmail -t -i
 2003-06-27 14:06:18 19W0QE-0001Nr-1b nobody@yourserversname.com from env-from
                     rewritten as ""usersite.com" <minx@usersite.com>" by rule 1

The message above tells me where the message came from, who sent it from my
server, the user and the path it was called from. It also tells me how it was
called and what it was renamed to before leaving my server.

The message below, tells me an incoming message arrived with the subject line
= “Naked Newsreaders? OH YEAH!”. Very helpful in determining spam. You will see
many other messages in exim_mainlog that you didn’t see before. Great for
debugging your message logs and catching spammers!

::

 EG: 19W0bO-0001cY-Ej <= jessica@stripdownnews.com H=(one) [128.121.247.84]:52087
                      I=[64.246.38.122]:25 P=smtp S=2387
                      T="Naked Newsreaders? OH YEAH!" from jessica@stripdownnews.com

**cPanel Servers**

If your server is running cPanel, the instructions are very simple.

1. Login WHM and go to Service Configuration / Exim Configuration Editor
2. Click the “Switch to Advanced Mode” button
3. Now you’ll see the WHM Exim configuration editor. This is essentially like
   editing exim.conf but throught he online interface and it
   will remember your changes where as if you edit the file directly through
   shell it will not.
4. In the first window which is empty you’ll need to insert the following:
   log_selector=+all
5. Go to the bottom and Save the changes, they will be applied and Exim will
   restart.
6. Success! You have added additioinal logging to your Exim mail server for
   better tracking.

**Non-cPanel Servers running Exim**

    1. Open /etc/exim.conf
       ::

        pico /etc/exim.conf

    2. Find this
       ::

        Ctrl + W: hostlist auth_relay_hosts = *
        #########################
        Runtime configuration file for Exim #
        #########################

    3. After ``hostlist auth_relay_hosts = *`` add the following:
       ::

        log_selector = +address_rewrite +all_parents +arguments +connection_reject
                       +delay_delivery +delivery_size +dnslist_defer +incoming_interface
                       +incoming_port +lost_incoming_connection +queue_run +received_sender
                       +received_recipients +retry_defer +sender_on_delivery +size_reject
                       +skip_delivery +smtp_confirmation +smtp_connection +smtp_protocol_error
                       +smtp_syntax_error +subject +tls_cipher +tls_peerdn

    4. The final result should look like this:
       ::

        hostlist auth_relay_hosts = *

        log_selector = +address_rewrite +all_parents +arguments +connection_reject +delay_delivery
                       +delivery_size +dnslist_defer +incoming_interface +incoming_port
                       +lost_incoming_connection +queue_run +received_sender +received_recipients
                       +retry_defer +sender_on_delivery +size_reject +skip_delivery +smtp_confirmation
                       +smtp_connection +smtp_protocol_error +smtp_syntax_error +subject
                       +tls_cipher +tls_peerdn

        #######################################
        # Runtime configuration file for Exim #
        #######################################

    5. Save and restart Exim
       ::

         ctrl + X then Y
         /etc/init.d/exim restart

Then you’re done!

.. disqus::
