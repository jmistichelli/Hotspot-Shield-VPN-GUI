# Hotspot-Shield-VPN-GUI
This is a Python3 GUI for the Linux Hotspot Shield VPN application. There is no official GUI. Command line configuration is tedious. This one is easy to use. 

Requirements:
- Hotspot Shield VPN Linux installation package
- Python Pexpect module

vpngui.py - Main program

config.py - Configuration file that must be edited. It will contain your username, password and default VPN location. 
Example:
    vpnusername = 'your@email.here'
    vpnpassword = 'your_password_here'
    defaultlocation = 'US - United States'
