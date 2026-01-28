import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("=== DEBUG START ===")
print("BOT_TOKEN exists:", bool(BOT_TOKEN))
print("CHAT_ID:", CHAT_ID)
print("=== DEBUG END ===")

if not BOT_TOKEN or not CHAT_ID:
    raise Exception("Missing BOT_TOKEN or CHAT_ID")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "TEST_OK_FROM_GITHUB_ACTION"
}

response = requests.post(url, data=payload)

print("Status code:", response.status_code)
print("Response text:", response.text)

response.raise_for_status()
