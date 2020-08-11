datas = "170,60&160,48"

for data in datas.split("&"):
    data = data.split(",")
    h, w = data
    bmi = "%.2f" % (float(w) / (float(h)/100)**2)
    print(bmi)

