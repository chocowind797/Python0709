import random
import time


def getScore(p):
    if p == 'A':
        return 1
    elif p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    else:
        return p


poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"] * 4
random.shuffle(poker)

print(poker)
# Start
sum_user = getScore(poker.pop())
sum_com = getScore(poker.pop())
count_user = count_com = 1
print('已拿:', sum_user, "總分:", sum_user)
flag = 1

while True:
    if sum_user > 10.5:
        print("玩家爆了!!", sum_com)
        flag = 0
        break
    elif count_user == 5:
        print("玩家過五關!!")
        flag = 2
        break
    elif sum_user == 10.5:
        print("玩家10點半!!")
        flag = 1
        break

    ask = input("是否繼續發牌(y/n): ")
    if ask == 'n' or ask == 'N':
        break
    p = getScore(poker.pop())
    sum_user += p
    count_user += 1
    print('再拿:', p, "總分:", sum_user)


while True:
    time.sleep(1)
    if sum_com > 10.5:
        print("電腦爆了!!")
        if flag == 0:
            flag = 3
        break
    elif count_com == 5:
        print("電腦過五關!!")
        if flag != 2:
            flag = 0
        else:
            flag = 3
        break
    elif sum_com == 10.5:
        print("電腦10點半!!")
        if flag == 2:
            pass
        elif flag == 1:
            flag == 3
        break

    if sum_com >= 9:
        break
    elif (sum_com < 7) or (poker.count('A') + poker.count(2) + poker.count(3) >= 10 and sum_com <= 7.5) or (poker.count('A') + poker.count(2) >= 7 and sum_com <= 8.5):
        p = getScore(poker.pop())
        sum_com += p
        count_com += 1
        print("PC再拿:", p, "總分:", sum_com)

print("PC總分:", sum_com)
if flag == 3:
    print("平手")
elif flag:
    print("玩家win")
else:
    print("電腦win")
