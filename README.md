# Hotspot-Shield-VPN-GUI
This is a Python3 GUI for the Linux Hotspot Shield VPN application. There is no official GUI. Command line configuration is tedious. This one is easy to use. 

Requirements:
 - Hotspot Shield VPN Linux installation package
 - Python Pexpect module

 # vpngui.py
 Main program. Runs the GUI.
 - Checks to see if the VPN is already in the active state.
 - Prompts for Username, Password and VPN termination location. Location defaults to "US - United States".
 - Presents the option to start VPN if not started, and to stop the VPN if started, with one button. 
 - Displays the status of the VPN (connected/notconnected) and IP/location information related to VPN termination point.

 Notes:
 - You can exit the vpngui.py app and, by default, the VPN will stay connected until VPN timers expire or there is a service interuption.
 - If the VPN is active and you want to change the VPN location you must stop the VPN first, choose the new location, then start the VPN again.
 
 # config.py
 Configuration file that must be initially edited. It will contain your default username, password and VPN location.
 
 Example:
 
    vpnusername = 'your@email.here'
    
    vpnpassword = 'your_password_here'
    
    defaultlocation = 'US - United States'
