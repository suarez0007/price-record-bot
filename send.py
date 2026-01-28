import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("BOT_TOKEN exists:", bool(BOT_TOKEN))
print("CHAT_ID:", CHAT_ID)

if not BOT_TOKEN or not CHAT_ID:
    print("❌ Missing BOT_TOKEN or CHAT_ID")
    exit(0)

message = "TEST_OK_123_FROM_GITHUB"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)

print("Status code:", response.status_code)
print("Response text:", response.text)
