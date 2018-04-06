What is Hotlink Protection?
===========================

Hotlink protection is an optional feature to the LSN CDN that allows you to
protect your bandwidth by disallowing other domains from linking to content
(images/videos/files) you have on the CDN.

**Block Hotlinking By Default**

1. Login to OnePortal’s cdn.html" target="_blank">CDN setup page.
2. Click “Modify Hotlink Policy”
3. Click “Block All By Default”
4. Click “Add Domain” and add all domains and subdomains you want to be able
   to link to your content.

  - Example: limestonenetworks.com
  - Example: www.limestonenetworks.com

5. Click “Save Changes” after each domain you add.
6. After adding all the domains you want to enable hotlinking for, click
   “Save Changes”

**Block only Certain Domains**

1. Login to OnePortal’s cdn.html" target="_blank">CDN setup page.
2. Click “Modify Hotlink Policy”
3. Click “Allow By Default”
4. Click “Add Domain” and add all domains and subdomains you want to block from
   linking to your content.

  - Example: bad-domain.com
  - Example: www.bad-domain.com

5. Click “Save Changes” after each domain you add.
6. After adding all the domains you want to block hotlinking for, click “Save
   Changes”

**Disable Hotlink Protection**

Hotlink protection is disabled by default, however, if you have enabled it then
you can disable it by doing the following.

1. Login to OnePortal’s cdn.html" target="_blank">CDN setup page.
2. Click “Modify Hotlink Policy”
3. Select “Allow All By Default”
4. Click the red “[X]” next to each domain. If you do not, those domains will
   be blocked.
5. When finished, press “Save Changes”
