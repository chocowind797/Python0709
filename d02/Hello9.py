print("BMI 系統")

name = input("請輸入名稱: ")
h = float(input("請輸入身高(cm): "))
w = float(input("請輸入體重(kg): "))

bmi = w / (h / 100) ** 2

result = '正常' if 18 <= bmi < 23 else '過高' if bmi >= 23 else '過低'

print("%s的身高是 %5.1fcm 體重是 %5.1fkg BMI 計算結果為 %5.2f (%s)" % (name, h, w, bmi, result))
