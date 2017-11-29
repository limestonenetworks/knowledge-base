Configuring Softaculous with WHMCS to Auto Install Client Websites
==================================================================

This guide will help you integrate your Softaculous installation with WHMCS to automate your web hosting business. This can only be configured with WHM servers and DirectAdmin servers currently.

**Install the Hook in WHMCS**

1. Download the Softaculous Auto Installation Hook. It is available from WHMCS Community Addons
2. Extract the file softaculous.php and upload it to /full_path_to/whmcs/includes/hooks/
3. Optionally, upload the file softaculous_debug.php to /full_path_to/whmcs/includes/hooks/
4. Remove the file softaculous_debug.php from the hooks directory after testing

Note: The softaculous_extra.php file adds Auto Installation capabilities for custom scripts. Otherwise, you do not need to upload this file.

**Activating the Hook with Your Hosting Plans**

1. Login to your WHMCS administrative panel.
2. Go to Setup -> Products/Services -> Products/Services and select the Icon to edit the hosting plan for automated installs
3. Under the Custom Fields tab, you will need to add 4 custom fields
  
  1. Custom Field #1

    1. Field Name: Script
    2. Field Type: Drop Down
    3. Description: Select the script to install
    4. Validation:
    5. Select Options: (comma-separated scripts list)**

  2. Custom Field #2

    1. Field Name: Admin Name
    2. Field Type: Text Box
    3. Description: Select your Admin Name for the script
    4. Validation:
    5. Select Options:

  3. Custom Field #3

    1. Field Name: Admin Pass
    2. Field Type: Text Box
    3. Description: Select your Admin Pass for the script
    4. Validation:
    5. Select Options:

  4. Custom Field #4

    1. Field Name: Admin Pass
    2. Field Type: Text Box
    3. Description: Select the directory you want to install the script at
    4. Validation:
    5. Select Options:

4. For the Hook to work properly, the custom fields should be entered exactly as above

**Here is a list of popular scripts, which are comma-separated for your convenience:**

None, WordPress, b2evolution, StatusNet, Drupal, Mambo, phpBB, SMF, AEF, Coppermine, Gallery, Jcow, OpenClassifieds, openX, WebCalendar, Shadows Rising, phpList, SquirrelMail, LimeSurvey, Piwik, SugarCRM, PHProjekt, osCommerce, Magento, phpBook, HESK, osTicket, kPlaylist, VidiScript, Gregarius, CodeIgniter, Moodle, Elgg

**Setup when the Module Runs**

The Hook will run to auto install the scripts only when an account is being created. To modify when this takes place, go to Setup -> Products/Services -> Products/Services and choose the hosting plan for automation. Then under the module settings tab you will see:

Setup when the automation runs

Select your desired settings and hit the “Save Changes” button.

**Testing the Module**

Initiate an order from a Dummy Account. Ensure that the Admin Name and Admin Pass are setup and that a script is selected.

Then click on the “Create” button to create the order.

You should see a box on the page that reads: “Are you sure you want to run the create function?”

Confirm this action by clicking the “Yes” button.

If the module was successful, you will see the message “Script Installed successfully”

If the hook was unsuccessful, you will see “Installation not completed” followed by the error given

When you are finished testing the module, remove the softaculous_debug.php file from your WHMCS installation
