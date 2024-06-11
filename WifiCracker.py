# WifiCracker
# A simple tool which captures saved wifi passwords and save to a text file.
# Author - WireBits

import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

with open("wifi_details.txt", 'a') as f:
    f.write("{:<30}|  {:<}".format("Wifi", "Password") + "\n")
    f.write("______________________________________________" + "\n")
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
                        'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        with open("wifi_details.txt", 'a') as f:
            f.write("{:<30}|  {:<}".format(i, results[0]) + "\n")
    except IndexError:
        with open("wifi_psk.txt", 'a') as f:
            f.write("{:<30}|  {:<}".format(i, ""))
