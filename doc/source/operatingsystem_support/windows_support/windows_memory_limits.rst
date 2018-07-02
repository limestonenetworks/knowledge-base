Windows Memory Limits
=====================

The table below describes the psychical memory limits supported by each Windows
version. We want to make sure our clients are aware of these limits as we begin
to offer increased amounts of RAM across our server platforms.
::

 Version                     32bit Limit        64bit Limit
 Windows 2008 Standard R2      n/a               32GB
 Windows 2008 Enterprise R2    n/a                2TB
 Windows 2008 Datacenter R2    n/a                2TB
 Windows 2012 Standard         n/a                4TB
 Windows 2012 Enterprise       n/a                n/a
 Windows 2012 Datacenter       n/a                4TB
 Windows 2016 Standard         n/a               24TB
 Windows 2016 Datacenter       n/a               24TB


We recommend that servers using more than 4GB of RAM install a 64bit operating
system over a 32bit operating system with PAE support.

`microsoft_memory_limit <https://msdn.microsoft.com/en-us/library/aa366778(v=vs.85).aspx>`_

`microsoft_PAE <https://msdn.microsoft.com/en-us/library/aa366796(v=vs.85).aspx>`_

.. disqus::
