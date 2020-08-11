def getBMI(h, w):
    return w / (h / 100)**2


bmi = getBMI(170, 60)
print("%.2f" % bmi)

bmi = getBMI(180, 70)
print("%.3f" % bmi)

bmi = getBMI(160, 50)
print("%.1f" % bmi)
