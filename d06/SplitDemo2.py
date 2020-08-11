datas = "170,60&160,48"

for data in datas.split("&"):
    data = data.split(",")
    bmi = "%.2f" % (float(data[1]) / (float(data[0])/100)**2)
    print(bmi)
