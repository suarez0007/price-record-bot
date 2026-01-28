import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

text = "TEST_FROM_GITHUB_ACTION"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": text
}

resp = requests.post(url, data=payload)

print("Status code:", resp.status_code)
print("Response text:", resp.text)

# 强制失败，方便你在 Actions 里看到
resp.raise_for_status()
