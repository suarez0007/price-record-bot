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

# 周一=0 … 周日=6
weekday_index = now.weekday()

# 读取 message.txt
with open("message.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 按 === 分割为多段
blocks = [block.strip() for block in content.split("===") if block.strip()]

if len(blocks) < 7:
    raise Exception("message.txt 至少需要 7 段内容（用 === 分隔）")

# 取今天对应的那一段
text = blocks[weekday_index]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": text,
    "disable_web_page_preview": True
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)

response.raise_for_status()
