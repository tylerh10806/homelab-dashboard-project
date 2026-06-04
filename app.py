import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SERVICES = [
    {"name": "pve-infra", "url": os.getenv("PVE_INFRA_URL")},
    {"name": "pve-apps", "url": os.getenv("PVE_APPS_URL")},
    {"name": "pve-services", "url": os.getenv("PVE_SERVICES_URL")},
    {"name": "pve-ripper", "url": os.getenv("PVE_RIPPER_URL")},
    {"name": "TrueNAS", "url": os.getenv("TRUENAS_URL")},
    {"name": "AdGuard", "url": os.getenv("ADGUARD_URL")},
    {"name": "Grafana", "url": os.getenv("GRAFANA_URL")},
    {"name": "Immich", "url": os.getenv("IMMICH_URL")},
    {"name": "Vaultwarden", "url": os.getenv("VAULTWARDEN_URL")},
    {"name": "Forgejo", "url": os.getenv("FORGEJO_URL")},
    {"name": "CBB Predictor", "url": os.getenv("CBB_URL")},
]

def check_service(url):
    try:
        response = requests.get(url, timeout=3, verify=False)
        return response.status_code < 500
    except:
        return False

@app.route("/")
def index():
    results = []
    for service in SERVICES:
        status = check_service(service["url"])
        results.append({
            "name": service["name"],
            "url": service["url"],
            "status": status
        })
    return render_template("index.html", services=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)