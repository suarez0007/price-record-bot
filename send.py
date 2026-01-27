import requests
import os
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

with open("messages.txt", "r", encoding="utf-8") as f:
    messages = [m.strip() for m in f.read().split("===") if m.strip()]

# 以日期作为索引：第 1 天发第 1 条
day_index = datetime.utcnow().toordinal() % len(messages)
text = messages[day_index]

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": text
}

requests.post(url, data=payload)
