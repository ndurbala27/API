from urllib.request import urlopen, Request
import json

def post_data():
    payload = {"name": "Ubuntu Student", "score": 95}
    data = json.dumps(payload).encode('utf-8')

    req = Request("http://localhost:8000/api/data", data=data, method="POST")
    req.add_header('Content-Type', 'application/json')

    try:
        with urlopen(req) as response:
            result = response.read().decode()
            print("✅ POST Response:", result)
    except Exception as e:
        print("❌ Error during POST:", e)

def get_data():
    try:
        with urlopen("http://localhost:8000/api/data") as response:
            data = json.loads(response.read().decode())
            print("📦 Stored Data:", data)
    except Exception as e:
        print("❌ Error during GET:", e)

if __name__ == '__main__':
    post_data()
    get_data()
