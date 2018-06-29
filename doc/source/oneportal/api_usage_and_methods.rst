API Usage and Methods  Most Helpful Article
===========================================

**API Usage**

All customers can use POST or GET to obtain or send data to our API. In
addition, any customer that chooses to use the API must add the IP address of
the system attempting to access the API in the Control Panel -> Administrative
-> API portion of their control panel. After adding an IP to the list of
authorized hosts in your API control panel you will see the API key next to
the IP address in the list. This API key is specific to this IP address and
your server control panel account.

You MUST edit the privileges of the newly added IP if you want it to be able to
access the API’s methods.

The base URL is:
::

 https://one.limestonenetworks.com/webservices/clientapi.php?key=YOURAPIKEY

An example would be:
::

 https://one.limestonenetworks.com/webservices/clientapi.php?key=YOURAPIKEY&mod=billing&action=getbalance

The request above from an authorized host would return your account’s current
balance.



**Returned Data Samples**

Data returned from the API is in basic XML format. The following are examples
of the data returned for each of the methods and their respective actions.

**Billing**

The ‘getbalance’ action will return your client ID and account balance, the
value expressed is USD.
::

 <source lang="xml">
     <client id="2XXX">
         <balance>0.00</balance>
     </client>
 </source>

The ‘history’ action will return a list of invoices. Each invoice includes the
date of invoice, due date, short description, status, and list of payments
pertaining to each invoice. A paid invoice will have an
invoices->invoice->status of completed.
::

 <invoices>
   <invoice id="1XXX1">
     <type>Debit</type>
     <created>2008-12-17 15:04:44</created>
     <unix_created>1229547884</unix_created>
     <duedate>0000-00-00</duedate>
     <unix_duedate>0</unix_duedate>
     <forserver>LSN-D0000</forserver>
     <description>New Server Order</description>
     <amount>136.74</amount>
     <status>completed</status>
     <payments>
       <payment id="1XXXX2">
         <method>PayPal</method>
         <txnid>9SA0000000000000X</txnid>
         <amount>136.74</amount>
       </payment>
      </payments>
   </invoice>
 </invoices>

**Servers**

The ‘list’ action will return the list of servers available in the control
panel. The list includes each server’s ID, display name, public/private ips,
power/port status, and bandwidth usage.
::

 <servers>
  <server id="LSN-D0000">
    <displayname>ServerName</displayname>
    <publicip>74.63.000.000</publicip>
    <privateip>10.2.000.000</privateip>
    <powerstatus>on</powerstatus>
    <bandwidth>
      <actual>
        <percentage>9.62</percentage>
        <bytes>192479575610</bytes>
        <friendly>192.5GB</friendly>
        <allocated>2000GB</allocated>
      </actual>
      <predicted>
        <percentage>70.87</percentage>
        <bytes>1417495092920</bytes>
        <friendly>1.4TB</friendly>
      </predicted>
    </bandwidth>
    <portstatus>
      <public>on</public>
      <private>on</private>
    </portstatus>
  </server>
 </servers>

**Code Samples**

The following are some simple examples of how to query data from the API.

**Simple PHP Example**

The following example requires the simplexml_load_file function which is
included with PHP5 but not PHP4.
::

 $apiKeyList = array(
    "exampleapikeynumber1",
    "exampleapikeynumber2"
 )

 foreach ($apiKeyList as $apiKey) {
    $apiData = "https://one.limestonenetworks.com/webservices/clientapi.php?key=".$apiKey."&mod=servers&action=list"

    $serverList = simplexml_load_file($apiData)

    foreach ($serverList->server as $serverItem) {
        print "<ul>"
        ."<li>Server ID = {$serverItem->attributes()->id}"
        ."<li>Server Name = {$serverItem->displayname}"
        ."<li>Server Public IP = {$serverItem->publicip}"
        ."<li>Server Bandwidth Used =
           {$serverItem->bandwidth->actual->friendly}"
        ."</ul>"
     }
 }

 unset($apiKey);

.. disqus::
