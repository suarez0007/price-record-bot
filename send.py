import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

text = """【价格记录｜仅供参考】

商品：菠菜刀削面 110g × 6 包
参考价：19.9 元

说明：
- 信息仅记录国内平台价格变化
- 商品仅支持中国大陆收货
- 非代购 / 非交易 / 不参与售后
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": text
}

requests.post(url, data=payload)
