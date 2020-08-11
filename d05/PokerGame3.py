import random
import time


def getScore(p):
    if p == 'A':
        return 1
    elif p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return p  # 2~10的數字


pokerAmount = 6
poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4 * pokerAmount
random.shuffle(poker)  # 洗牌
flag = 3  # 0玩家輸 1玩家贏 2平手 3比大小
# 餘額
balance = 100

while True:
    # 下注
    bet = int(input("請下注(不可超過%d), 離開(-1): " % balance))
    if bet == -1:
        print("目前餘額:", balance)
        break
    elif bet > balance:
        print("下注金額過大,請重新下注!!")
        continue
    # 牌局開始先發一張
    p1 = poker.pop()
    sum1 = getScore(p1)
    print('已拿:', p1, '總分:', sum1)

    # 繼續拿牌 ?
    count_user = 1
    while True:
        ask = input('是否要拿牌(y/n)? ')
        if ask == 'y':
            p = poker.pop()
            sum1 += getScore(p)
            print('再拿:', p, '總分:', sum1)
            if sum1 > 10.5:
                print('User 爆了')
                flag = 0
                break
            elif sum1 == 10.5:
                print('十點半!!')
                flag = 1
            else:
                count_user += 1
            if count_user == 5:
                print('User 過五關, 超強的~~~')
                flag = 1
                break
        else:
            break

    # PC 拿牌
    count_pc = 1
    p2 = poker.pop()
    sum2 = getScore(p2)
    print('PC已拿:', p2, '總分:', sum2)

    while True:
        take = False  # 是否拿牌?
        time.sleep(2)  # 延遲 2 秒
        if sum2 >= 9:  # 電腦若為 9 點（含）以上不需補牌
            break
        elif sum2 < 7:  # 電腦少於 7 點點需強迫補牌
            take = True
        elif sum2 == 7 or sum2 == 7.5:
            amount = poker.count('A') + poker.count(2) + poker.count(3)
            if amount >= 10*pokerAmount:
                take = True
        elif sum2 == 8 or sum2 == 8.5:
            amount = poker.count('A') + poker.count(2)
            if amount >= 7*pokerAmount:
                take = True

        if sum2 > sum1 or flag == 0:
            take = False

        # 是否拿牌 ?
        if take:
            p = poker.pop()
            sum2 += getScore(p)
            print('PC再拿:', p, '總分:', sum2)

        # 判斷是否爆了 ?
        if sum2 > 10.5:
            print('PC 爆了')
            if flag == 0:
                flag = 2
            else:
                flag = 1
            break
        elif sum2 == 10.5:
            print('PC 十點半!!')
            if flag == 1:
                flag = 2
            elif flag == 3:
                flag = 0
        else:
            count_pc += 1

        # 判斷是否過五關 ?
        if count_pc == 5:
            print('PC 過五關, 超強的~~~')
            if flag == 1:
                flag = 2
            elif flag != 4:
                flag = 0
            break

    if flag == 3:
        if sum1 == sum2:
            flag = 2
        elif sum1 > sum2:
            flag = 1
        else:
            flag = 0

    if flag == 0:
        if count_pc == 5:
            bet *= 3
        balance -= bet
        print("電腦贏, 最新餘額:", balance)
    elif flag == 1:
        if count_user == 5:
            bet *= 3
        balance += bet
        print("玩家贏, 最新餘額:", balance)
    else:
        print("平手, 最新餘額:", balance)

    if balance <= 0:
        print("破產!!!")
        break
    print()
