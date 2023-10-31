import tkinter as tk
from tkinter import *
from tkinter import ttk
import config as config
import subprocess
import pexpect
import time
import ast


root = tk.Tk()

# create main window
root.geometry("400x600")
root.title("Hotspot Shield VPN")
root.config(padx=20, pady=20)

global startbutton
global stopbutton
global locationselected


def run_command(command):
    rawoutput = subprocess.check_output(command.split())
    statuslbl.config(text=rawoutput.decode("utf-8"))


def get_ipinfo():
    bin_ipinfo = subprocess.check_output('curl ipinfo.io'.split())
    ipinfo = ast.literal_eval(bin_ipinfo.decode("utf-8"))
    return f'IP: {ipinfo["ip"]}\nCity: {ipinfo["city"]}\nCountry: {ipinfo["country"]}'


def print_status():
    rawoutput = subprocess.check_output('hotspotshield status'.split())
    statuslbl.config(text=rawoutput.decode("utf-8"))
    iplabel.config(text=get_ipinfo())


def start_vpn():
    child = pexpect.spawn('hotspotshield account signin')
    child.expect('Username: ')
    child.sendline(config.vpnusername)
    child.expect('Password: ')
    child.sendline(config.vpnpassword)
    time.sleep(1)
    location = drop.get().split(" ")
    subprocess.run(["hotspotshield", "connect", location[0]])
    startbutton.grid_forget()
    stopbutton.grid(row=3, column=0, columnspan=2, pady=30)
    time.sleep(1)
    print_status()


def stop_vpn():
    subprocess.run(["hotspotshield", "disconnect"])
    stopbutton.grid_forget()
    startbutton.grid(row=3, column=0, columnspan=2, pady=30)
    print_status()


def getlocations():
    locations_output = subprocess.check_output("hotspotshield locations".split())
    locationlist = locations_output.decode("utf-8").splitlines()

    del (locationlist[0])
    del (locationlist[0])
    i = 0
    for item in locationlist:
        locationlist[i] = item.replace(' ', '-', 1)
        i += 1
    i = 0
    for item in locationlist:
        locationlist[i] = item.replace(' ', '')
        i += 1
    i = 0
    for item in locationlist:
        locationlist[i] = item.replace('-', ' - ')
        i += 1

    return locationlist


userlbl = tk.Label(root, text="Username:")
userlbl.grid(row=0, column=0)

passlbl = tk.Label(root, text="Password:")
passlbl.grid(row=1, column=0, pady=5)

loclbl = tk.Label(root, text="Location:")
loclbl.grid(row=2, column=0, pady=5)

# single line input box
usernameentry = tk.Entry(root)
usernameentry.grid(row=0, column=1, pady=5)
usernameentry.insert(0, config.vpnusername)
passwordentry = tk.Entry(root, show='*')
passwordentry.grid(row=1, column=1, pady=5)
passwordentry.insert(0, config.vpnpassword)

drop = ttk.Combobox(root, values=getlocations(), state="readonly")
drop.set(config.defaultlocation)
drop.grid(row=2, column=1, pady=5)

vpn_status_output = subprocess.check_output("hotspotshield status".split())
vpn_status = vpn_status_output.decode("utf-8")


# create a button
startbutton = tk.Button(root, text="Start VPN", font=('Arial bold', 20), command=start_vpn)
stopbutton = tk.Button(root, text="Stop VPN", font=('Arial bold', 20), command=stop_vpn)


if "VPN connection state : connected" in vpn_status:
    startbutton.grid_forget()
    stopbutton.grid(row=3, column=0, columnspan=2, pady=30)
else:
    stopbutton.grid_forget()
    startbutton.grid(row=3, column=0, columnspan=2, pady=30)


statuslblfrm = ttk.LabelFrame(root, text="Status:")
statuslblfrm.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)

statuslbl = tk.Label(statuslblfrm, text="", anchor='w')
statuslbl.grid(row=0, column=0, sticky=tk.W)

iplabel = tk.Label(statuslblfrm, text='')
iplabel.grid(row=1, column=0, sticky=tk.W)

print_status()

root.mainloop()
