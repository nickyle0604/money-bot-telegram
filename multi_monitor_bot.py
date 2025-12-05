import time
from tabulate import tabulate
from market_utils import get_price
from telegram_utils import send_telegram_message

# ====== CẤU HÌNH ======
SYMBOLS = ["BTCUSDT", "ETHUSDT", "LINKUSDT", "BNBUSDT"]
ALERT_THRESHOLD = 1.0  # % biến động để gửi alert

BOT_TOKEN = "8119671883:AAFWhDPhryZnmLKv6RZmvbiMUItEo3H9hKc"
CHAT_ID = 1333105427

# ======================

def color_pct(pct: float) -> str:
    if pct > 0:
        return f"\033[92m{pct:.2f}%\033[0m"
    elif pct < 0:
        return f"\033[91m{pct:.2f}%\033[0m"
    else:
        return f"{pct:.2f}%"


def main():
    print("=== MULTI-COIN MONITOR + TELEGRAM ALERT ===")
    print("Lấy giá base...")

    base_prices = {}
    for sym in SYMBOLS:
        price = get_price(sym)
        base_prices[sym] = price
        print(f"{sym} base = {price}")

    alerted = {sym: False for sym in SYMBOLS}

    print("\nBắt đầu theo dõi. Nhấn Ctrl + C để dừng.\n")

    while True:
        rows = []
        for sym in SYMBOLS:
            current = get_price(sym)
            base = base_prices[sym]
            change_pct = (current - base) / base * 100

            rows.append([sym, base, current, color_pct(change_pct)])

            if abs(change_pct) >= ALERT_THRESHOLD and not alerted[sym]:
                text = (
                    f"⚠️ {sym} biến động mạnh!\n"
                    f"Giá base: {base:.4f}\n"
                    f"Giá hiện tại: {current:.4f}\n"
                    f"Thay đổi: {change_pct:.2f}%"
                )
                send_telegram_message(BOT_TOKEN, CHAT_ID, text)
                alerted[sym] = True

            if abs(change_pct) < ALERT_THRESHOLD * 0.5:
                alerted[sym] = False

        print("\033c", end="")
        print("=== MONITOR (so với giá base) ===")
        print(tabulate(
            rows,
            headers=["Symbol", "Base", "Current", "Change %"],
            floatfmt=".4f"
        ))
        print(f"\nNgưỡng alert: {ALERT_THRESHOLD}% (gửi Telegram)\n")

        time.sleep(5)


if __name__ == "__main__":
    main()
