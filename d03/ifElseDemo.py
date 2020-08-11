def printBMI(h, w):
    bmi = w / (h / 100)**2
    result = "過重" if bmi >= 23 else "過輕" if bmi < 18 else "正常"
    print("身高: %.1f 體重: %.1f BMI: %.2f (%s)" % (h, w, bmi, result))


printBMI(170.5, 60.3)
printBMI(180.5, 70.3)
printBMI(160.5, 50.3)
