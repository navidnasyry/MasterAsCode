import requests
import base64
import json

DITTO_URL = "http://localhost:8080/api/2/things"
USERNAME = "ditto"
PASSWORD = "ditto"
AUTH = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Basic {AUTH}"
}

def create_thing(index):
    thing_id = f"nasa.jet.engine:{index}"

    payload = {
        "definition": "com.nasa:jetengine:1.0.0",
        "attributes": {
            "dataset": "NASA Jet Engine Dataset",
            "status": "On"
        },
        "features": {
            "engine-data": {
                "properties": {
                    "rpm": 0,
                    "temperature": 0,
                    "pressure": 0
                }
            }
        }
    }

    url = f"{DITTO_URL}/{thing_id}"
    response = requests.put(url, headers=HEADERS, data=json.dumps(payload))

    if response.status_code in (200, 201):
        print(f"Created thing: {thing_id}")
    else:
        print(f"Failed to create {thing_id}: {response.status_code} {response.text}")


if __name__ == "__main__":
    for i in range(1, 101):
        create_thing(i)

