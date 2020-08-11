import random
import sys

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
chance = 0

while True:
    if chance % 2 == 0:
        if sum_com > 10.5:
            print("玩家爆了!!", sum_user)
            break
        elif count_com == 5:
            print("玩家過五關!!")
            break
        elif sum_com == 10.5:
            print("玩家10點半!!")
            break

        ask = input("是否繼續發牌(y/n): ")
        if ask == 'n' or ask == 'N':
            chance = 1
            continue
        p = getScore(poker.pop())
        sum_user += p
        count_user += 1
        print('再拿:', p, "總分:", sum_user)

    else:
        if sum_user > 10.5:
            print("電腦爆了!!", sum_com)
            break
        elif count_user == 5:
            print("電腦過五關!!")
            break
        elif sum_user == 10.5:
            print("電腦10點半!!")
            break

        print("按下Enter換電腦")
        sys.stdin.read(1)
        sum_com += getScore(poker.pop())
        count_com += 1

    chance += 1
