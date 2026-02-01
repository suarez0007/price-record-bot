import os
import requests
from datetime import datetime, timedelta, timezone

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise Exception("缺少 BOT_TOKEN 或 CHAT_ID")

# 北京时间
beijing_tz = timezone(timedelta(hours=8))
now = datetime.now(beijing_tz)
weekday_index = now.weekday()

# ===== 关键修复：绝对路径 =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MESSAGE_PATH = os.path.join(BASE_DIR, "messages.txt")

with open(MESSAGE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

blocks = [b.strip() for b in content.split("===") if b.strip()]

if len(blocks) < 7:
    raise Exception("message.txt 至少需要 7 段内容")

text = blocks[weekday_index]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": text,
    "disable_web_page_preview": True
}

r = requests.post(url, json=payload)
print(r.text)
r.raise_for_status()
