ttt = [['O', 'O', 'X'],
       ['X', 'O', ' '],
       ['X', ' ', 'X']
       ]

for tt in ttt:
    print(tt)
print()

pos = int(input("請輸入位置(0~8): "))
ttt[pos // 3][pos % 3] = 'O'

for tt in ttt:
    print(tt)
