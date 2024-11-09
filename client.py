import requests
import json
from datetime import datetime

# The URL of your Node.js server
url = "http://localhost:3000/data"

# Sample data (timestamp and water level)
data = {
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "water_level": 45.6,  # Example water level
}

# Send a POST request with the JSON data
try:
    response = requests.post(url, json=data)

    # Check if the response is successful
    if response.status_code == 200:
        print("Data successfully sent!")
        print("Server Response:", response.json())
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
        print("Error:", response.json())

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
