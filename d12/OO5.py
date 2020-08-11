class Order:
    # 地區 國家 項目 類型 銷售渠道 訂單優先 訂單日期 訂單ID 發貨日期 售出單位  單價 單位成本 總收入 總成本 總利潤
    region = ""
    country = ""
    itemType = ""
    salesChannel = ""
    orderPriority = ""
    orderDate = ""
    orderID = ""
    shipDate = ""
    unitsSold = ""
    unitPrice = ""
    unitCost = ""
    totalRevenue = ""
    totalCost = ""
    totalProfit = ""

    def __init__(self, region, country, itemType, salesChannel,
                 orderPriority, orderDate, orderID, shipDate,
                 unitsSold, unitPrice, unitCost, totalRevenue,
                 totalCost, totalProfit
                 ) -> None:
        self.region = region
        self.country = country
        self.itemType = itemType
        self.salesChannel = salesChannel
        self.orderPriority = orderPriority
        self.orderDate = orderDate
        self.orderID = orderID
        self.shipDate = shipDate
        self.unitsSold = unitsSold
        self.unitPrice = unitPrice
        self.unitCost = unitCost
        self.totalRevenue = totalRevenue
        self.totalCost = totalCost
        self.totalProfit = totalProfit


if __name__ == '__main__':
    file = open("10000 Sales Records.csv", 'r')
    dataList = []
    for data in file.readlines():
        rows = data.split(",")
        if data.__contains__('Region'):
            continue
        if data.__contains__('Taiwan'):
            order = Order(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8], rows[9],
                          rows[10], rows[11], rows[12], rows[13])
            dataList.append(order)

    for order in dataList:
        print(order.country, order.itemType, order.totalRevenue)
