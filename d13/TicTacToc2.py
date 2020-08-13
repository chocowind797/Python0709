import random as r
import time

ttt = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']
       ]


def check(name):
    space = 0
    for tt in ttt:
        for t in tt:
            if t == ' ':
                space += 1

    if space == 0:
        return False

    flag = False
    for i in range(3):
        if ttt[i][0] == ttt[i][1] == ttt[i][2] != ' ':
            flag = True
        elif ttt[0][i] == ttt[1][i] == ttt[2][i] != ' ':
            flag = True
    if ttt[0][0] == ttt[1][1] == ttt[2][2] != ' ':
        flag = True
    elif ttt[0][2] == ttt[1][1] == ttt[2][0] != ' ':
        flag = True
    if flag:
        print(name + " Win!!")
        return "end"


def play():
    for tt in ttt:
        print(tt)
    print()

    # 使用者
    pos = int(input("請輸入位置(0~8): "))
    ttt[pos // 3][pos % 3] = 'O'
    for tt in ttt:
        print(tt)
    print()

    space = check('player')
    if space == 'end':
        return
    if space is False:
        print("平手")
        return

    time.sleep(2)

    # 換電腦
    while True:
        pos = r.randint(0, 8)
        if ttt[pos // 3][pos % 3] == ' ':
            print("電腦選擇:", pos)
            ttt[pos // 3][pos % 3] = 'X'
            break

    space = check('com')
    if space == 'end':
        return
    if space is False:
        print("平手")
        return
play()


if __name__ == '__main__':
    play()
