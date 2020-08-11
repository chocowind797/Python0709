import RC
def calcBMI() -> None:
    h = float(input("請輸入身高(cm): "))
    w = float(input("請輸入體重(kg): "))
    bmi = w / (h / 100) ** 2
    result = "過重" if bmi >= 23 else "過輕" if bmi < 18 else "正常"
    print("身高: %.1f 體重: %.1f BMI: %.2f (%s)" % (h, w, bmi, result))


def menu() -> None:
    print("\tBMI 計算系統")
    print("===================")
    print("1. 輸入身高體重")
    print("2. 離開系統")
    mode = int(input("請選擇: "))
    while mode != 1 and mode != 2:
        print("選擇錯誤")
        mode = int(input("請選擇: "))
    print("===================")
    if mode == 2:
        print("您已離開系統!!")
        return
    else:
        print("您選擇的是 1")
        calcBMI()
        print("===================")
        input("按下任意鍵繼續...")
        print("===================\n")
        menu()


menu()
