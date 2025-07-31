#!/usr/bin/env python3

import os
import requests
from datetime import datetime

# Replace with your TimeZoneDB API key
API_KEY = 'REPLACE_WITH_YOUR_API_KEY'
ZONE = 'Asia/Colombo'

def is_connected():
    try:
        requests.get("http://clients3.google.com/generate_204", timeout=5)
        return True
    except:
        return False

def get_time_from_api():
    print("📡 Checking internet connection...")
    if not is_connected():
        print("❌ No internet connection.")
        return None

    print("✅ Internet connected.")
    url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={API_KEY}&format=json&by=zone&zone={ZONE}"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        if data.get("status") == "OK":
            timestamp = int(data["timestamp"])
            dt = datetime.fromtimestamp(timestamp)
            print(f"🕒 Current time in {ZONE}: {dt}")
            os.system(f"sudo date -s '@{timestamp}'")
        else:
            print(f"❌ API Error: {data.get('message')}")
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    get_time_from_api()
