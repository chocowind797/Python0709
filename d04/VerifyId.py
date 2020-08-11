# 轉換英文為數字
def getNum(char):
    if char == "A":
        return 10
    elif char == "B":
        return 11
    elif char == "C":
        return 12
    elif char == "D":
        return 13
    elif char == "E":
        return 14
    elif char == "F":
        return 15
    elif char == "G":
        return 16
    elif char == "H":
        return 17
    elif char == "I":
        return 34
    elif char == "J":
        return 18
    elif char == "K":
        return 19
    elif char == "L":
        return 20
    elif char == "M":
        return 21
    elif char == "N":
        return 22
    elif char == "O":
        return 35
    elif char == "P":
        return 23
    elif char == "Q":
        return 24
    elif char == "R":
        return 25
    elif char == "S":
        return 26
    elif char == "T":
        return 27
    elif char == "U":
        return 28
    elif char == "V":
        return 29
    elif char == "W":
        return 32
    elif char == "X":
        return 30
    elif char == "Y":
        return 31
    elif char == "Z":
        return 33


# 串接轉換後的英文和原數字
def getID(cord, id):
    return str(cord) + str(id)


# 將身分證字號轉換為數字
def getAll(id):
    sum = int(id[0]) + int(id[len(id)-1])
    for i in range(1, len(id)-1):
        sum += int(id[i]) * (9-i+1)
    return sum


# 檢查是否正確
def check(id):
    id = getAll(id)
    if id % 10 == 0:
        return True
    return False


# Main Method
while True:
    mode = int(input("1.確認身分證字號是否有效  2.身分證字號產生器  3.退出\n請選擇: "))
    print("===================")
    if mode == 1:
        id = input("輸入身分證字號: ")
        VerifyID = getID(getNum(id[0]), id[1:])

        if check(VerifyID) and (id[1] == "1" or id[1] == "2"):
            print("身分證字號正確")
        else:
            print("身分證字號錯誤")

        print("===================")
    elif mode == 2:
        import random

        while True:
            id = chr(random.randint(0, 25) + 65) + str(random.randint(1, 2))
            for i in range(8):
                id += str(random.randint(0, 9))
            VerifyID = getID(getNum(id[0]), id[1:])
            if check(VerifyID) and (id[1] == "1" or id[1] == "2"):
                break

        print(id)
        print("===================")
    elif mode == 3:
        print("已結束程式")
        break
    else:
        print("輸入錯誤!!")
        print("===================")
