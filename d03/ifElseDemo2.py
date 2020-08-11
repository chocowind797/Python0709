def getBMI(h, w):
    bmi = w / (h / 100)**2
    result = "過重" if bmi >= 23 else "過輕" if bmi < 18 else "正常"
    return h, w, bmi, result


h, w, bmi, result = getBMI(170.5, 60.3)
print("身高: %.1f 體重: %.1f BMI: %.2f (%s)" % (h, w, bmi, result))
