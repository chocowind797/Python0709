def add(x, y):
    print("執行到 add() 方法", x, y)
    return x + y


def info():
    print("執行到 info() 方法")
    print("本程式是由 Python 所撰寫")


def checkSex(id):
    sex = id[1]
    if sex == '1':
        print("男性")
        return
    if sex == '2':
        print("女性")
        return
    print("錯誤")


sum = add(10, 20)
print(sum)
checkSex("H323456789")
