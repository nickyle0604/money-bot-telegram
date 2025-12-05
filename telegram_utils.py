import requests

def send_telegram_message(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        r = requests.post(url, json=payload, timeout=10)
        print("Telegram status:", r.status_code, r.text)  # <- DÒNG NÀY RẤT QUAN TRỌNG
    except Exception as e:
        print("Lỗi gửi Telegram:", e)
