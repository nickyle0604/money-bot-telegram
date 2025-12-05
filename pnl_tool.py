from tabulate import tabulate

def calculate_pnl(amount, buy_price, sell_price):
    profit = (sell_price - buy_price) * amount
    return profit

orders = []

print("=== TOOL TÍNH LÃI/LỖ P2P ===")
while True:
    amount = float(input("Số lượng (USDT): "))
    buy = float(input("Giá mua: "))
    sell = float(input("Giá bán: "))

    pnl = calculate_pnl(amount, buy, sell)

    orders.append([amount, buy, sell, pnl])

    cont = input("Thêm lệnh nữa không? (y/n): ")
    if cont.lower() != "y":
        break

# In bảng kết quả
headers = ["Amount", "Buy", "Sell", "PnL"]

print("\n=== KẾT QUẢ ===")
print(tabulate(orders, headers=headers, floatfmt=".2f"))

# Tổng lãi/lỗ
total_pnl = sum(o[3] for o in orders)
print("\nTỔNG LÃI/LỖ:", round(total_pnl, 2))
