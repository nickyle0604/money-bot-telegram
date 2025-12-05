import time
from tabulate import tabulate
from market_utils import get_price

# Danh sách coin muốn theo dõi
SYMBOLS = ["BTCUSDT", "ETHUSDT", "LINKUSDT", "BNBUSDT"]

ALERT_THRESHOLD = 1.0  # % biến động để cảnh báo

def color_pct(pct: float) -> str:
    """Màu cho % thay đổi: xanh nếu tăng, đỏ nếu giảm."""
    if pct > 0:
        return f"\033[92m{pct:.2f}%\033[0m"   # xanh
    elif pct < 0:
        return f"\033[91m{pct:.2f}%\033[0m"   # đỏ
    else:
        return f"{pct:.2f}%"


def main():
    print("=== MULTI-COIN MONITOR ===")
    print("Lấy giá mở đầu phiên...")

    # 1) Lấy giá ban đầu làm mốc so sánh
    base_prices = {}
    for sym in SYMBOLS:
        price = get_price(sym)
        base_prices[sym] = price
        print(f"{sym} base = {price}")

    print("\nBắt đầu theo dõi. Nhấn Ctrl + C để dừng.\n")

    # 2) Vòng lặp monitor
    while True:
        rows = []
        alerts = []

        for sym in SYMBOLS:
            current = get_price(sym)
            base = base_prices[sym]
            change_pct = (current - base) / base * 100

            # tạo dòng cho bảng
            rows.append([sym, base, current, color_pct(change_pct)])

            # nếu biến động lớn thì thêm vào danh sách cảnh báo
            if abs(change_pct) >= ALERT_THRESHOLD:
                alerts.append((sym, change_pct))

        # Xoá màn hình đơn giản (không cần nhưng nhìn sẽ sạch)
        print("\033c", end="")

        # In bảng
        print("=== MULTI-COIN MONITOR (so với giá base) ===")
        print(tabulate(
            rows,
            headers=["Symbol", "Base", "Current", "Change %"],
            floatfmt=".4f"
        ))

        # In cảnh báo
        if alerts:
            print("\n⚠️  CẢNH BÁO BIẾN ĐỘNG LỚN:")
            for sym, pct in alerts:
                print(f" - {sym}: {pct:.2f}%")

        # ngủ 5 giây rồi lặp lại
        time.sleep(5)


if __name__ == "__main__":
    main()
