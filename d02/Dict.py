import random as r

mode = int(input("輸入 0(比小)l, 1(比大): "))

user = r.randint(1, 6) + r.randint(1, 6) + r.randint(1, 6)
pc = r.randint(1, 6) + r.randint(1, 6) + r.randint(1, 6)

if mode == 1:
    winner = "玩家" if user > pc else "電腦"
else:
    winner = "玩家" if user < pc else "電腦"

result = "比{}, 玩家的點數{}, 電腦的點數{}, 勝者:{}".format("大" if mode == 1 else "小", user, pc, winner)

print(result)
