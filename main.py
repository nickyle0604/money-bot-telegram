def calculate_pnl(amount, buy_price, sell_price):
    buy_cost = amount * buy_price
    sell_revenue = amount * sell_price
    profit = sell_revenue - buy_cost
    return profit

# Test thử
amount = 1000    # 1000 USDT
buy_price = 248  # giá mua LINK
sell_price = 251 # giá bán LINK

profit = calculate_pnl(amount, buy_price, sell_price)
print("Lợi nhuận:", profit)
