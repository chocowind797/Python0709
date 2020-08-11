report = "台積電目前價格每股315.5元,非常適合賣出4000股,目前我的庫存有6000股"
price = float(report[9:14])
cost = int(report[-5:-1]) - int(report[22:26])

print(price * cost)
