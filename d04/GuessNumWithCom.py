import random as r
import sys

small, big = 0, 100
# small, big = int(input("輸入最小值: ")), int(input("輸入最大值: "))

num = r.randint(small+1, big-1)
choice = 0

result = True
i = 0

while True:
    if i % 2 == 0:
        choice = int(input("請在 {} ~ {} 之間猜一數字: ".format(small, big)))
        if not (small < choice < big):
            print("{} 輸入範圍錯誤!!".format(choice))
            continue
        if choice == num:
            break
        print("按下Enter讓電腦猜!")
        sys.stdin.read(1)

    else:
        choice = r.randint(small+1, big-1)
        print("電腦在 {} ~ {} 之間猜一數字: {}".format(small, big, choice))
        if choice == num:
            result = False
            break
    i += 1
    if choice > num:
        big = choice
    elif choice < num:
        small = choice

print("使用者" if result else "電腦", "猜對了!!數字為:{}".format(num),sep="")
