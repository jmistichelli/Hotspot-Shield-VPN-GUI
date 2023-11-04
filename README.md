# Hotspot-Shield-VPN-GUI
This is a Python3 GUI for the Linux Hotspot Shield VPN application. There is no official GUI. Command line configuration is tedious. This one is easy to use. 

Requirements:
 - Hotspot Shield VPN Linux installation package (hotspotshield_1.0.7_amd64.deb)
 - Tkinter (sudo apt install python3-tk)
 - Pexpect module (pip install pexpect)
 - Curl module (sudo apt install curl)

   Note: All can be installed using included requirments.txt file (pip install -r /path/to/requirements.txt) 

 # vpngui.py
 Main program. Runs the GUI.
 - Checks to see if the VPN is already in the active state.
 - Prompts for Username, Password and VPN termination location. Location defaults to "US - United States".
 - Presents the option to start VPN if not started, and to stop the VPN if started, with one button. 
 - Displays the status of the VPN (connected/notconnected) and IP/location information related to VPN termination point.

 Notes:
 - You can exit the vpngui.py app and, by default, the VPN will stay connected until VPN timers expire or there is a service interuption.
 - If the VPN is active and you want to change the VPN location you must stop the VPN first, choose the new location, then start the VPN again.
 
 # vpnconfig.py
 Configuration file that must be initially edited. It will contain your default username, password and VPN location.
 
 Example:
 
    vpnusername = 'your@email.here'
    
    vpnpassword = 'your_password_here'
    
    defaultlocation = 'US - United States'

# hotspot-shield.desktop
This is the application shortcut. Copy this to the desktop. Right click on it and click 'Allow Launching'. The shortcut assumes you have the python files in /usr/local/bin/. It also assumes you are using /usr/share/icons/HighContrast/48x48/status/network-wireless-hotspot.png as the icon. Adjust the contents as necessary to reflect the location and filenames in your implementation.
