Cloud Volumes
=============

**Volumes** act as detachable storage that can be connected to any of your VMs for storage or bootable media.
To create a new Volume Press the **“Create Volume”** Button in the Volumes tab of the control panel.

.. image:: /image/Volumes.jpg

.. image:: /image/createvolume.jpg

- Volume Name input the name of the volume here.
- Description input the description of the volume here.
- Volume source Select “No source, empty volume” if the volume will be used for storage only. If you would like the volume to be bootable you will need to select “Image” here. A new drop down box will appear and allow you to choose an image to be installed onto the volume.
- Use image as source To use the volume as bootable storage for a new VM you’ll need to select which OS to be installed. See this Link for details.
- Type allow you to choose SSD(Solid state drive) or HDD(Hard disk drive) as your storage type. SSD storage is faster but more expensive and HDD storage is slower but less expensive.
- Size allows you to choose the size of the volume in GBs.
- Availability Zone Currently there is only one option which is our Dallas location.

Press **“Create Volume”** to create the volume
Once created you can attach the volume to a VM using the drop down box under **“Actions”** With the **“Manage Attachments”** button.
