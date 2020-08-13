def inputNumber():
    try:
        x = int(input("請輸入數字: "))
        print("您輸入的是:", x)
    except Exception as e:
        print("輸入錯誤, 錯誤原因:", e)
        inputNumber()


if __name__ == '__main__':
    inputNumber()
