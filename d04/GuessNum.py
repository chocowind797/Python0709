import random as r

small, big = 0, 100
# small, big = int(input("輸入最小值: ")), int(input("輸入最大值: "))

num = r.randint(small+1, big-1)
choice = 0
times = 0
while choice != num and times != 5:
    choice = int(input("在 {} ~ {} 之間猜一數字: ".format(small, big)))
    if not(small < choice < big):
        print("{} 輸入範圍錯誤!!".format(choice))
        continue
    if choice > num:
        big = choice
    elif choice < num:
        small = choice
    times += 1

print("都錯" if choice != num else "猜對", "了!!數字為:{}".format(num),sep="")
