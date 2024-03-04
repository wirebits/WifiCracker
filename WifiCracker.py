# WifiCracker
# A simple tool which captures saved wifi passwords and save to a text file.
# Author - WireBits

import subprocess
import platform

def extract_wifi_info():
    system = platform.system()

    if system == "Windows":
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        with open("wifi_psk.txt", 'a') as f:
            f.write("{:<30}|  {:<}\n".format("Wifi", "Password"))
            f.write("______________________________________________\n")

        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

            try:
                with open("wifi_psk.txt", 'a') as f:
                    f.write("{:<30}|  {:<}\n".format(i, results[0]))
            except IndexError:
                with open("wifi_psk.txt", 'a') as f:
                    f.write("{:<30}|  {:<}\n".format(i, ""))

    elif system == "Linux":
        conf_path = '/etc/wpa_supplicant/wpa_supplicant.conf'
        try:
            with open(conf_path, 'r') as f:
                lines = f.readlines()
                ssid = None
                password = None
                for line in lines:
                    if line.strip().startswith('ssid='):
                        ssid = line.split('=')[1].strip().strip('"')
                    elif line.strip().startswith('psk='):
                        password = line.split('=')[1].strip().strip('"')
                    if ssid and password:
                        with open("wifi_psk.txt", 'a') as f:
                            f.write("{:<30}|  {:<}\n".format(ssid, password))
                            ssid = None
                            password = None
        except FileNotFoundError:
            print("Error: wpa_supplicant.conf file not found.")
        except Exception as e:
            print("Error:", e)

    else:
        print("Unsupported operating system")

extract_wifi_info()