import time
import random
import json
from datetime import datetime

LOG_FILE = "telemetry/logs.json"

def generate_data():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "speed_mph": random.randint(0, 120),
        "rpm": random.randint(700, 6500),
        "engine_temp_f": random.randint(160, 230),
        "fuel_level": random.randint(10, 100)
    }

def write_log(data):
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

while True:
    data = generate_data()
    print(json.dumps(data))
    write_log(data)
    time.sleep(2)
