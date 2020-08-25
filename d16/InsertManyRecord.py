import sqlite3
import random as r

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

lottos = []

for i in range(100):
    # 取出1 ~ 49 不重複的數字共 6 個
    nums = set()
    while len(nums) < 6:
        nums.add(r.randint(1, 49))
    lottos.append(tuple(nums))  # 要轉成元組(資料庫規定)
print(lottos)

# 多筆資料新增
cursor.executemany('insert into lotto(n1, n2, n3, n4, n5, n6) values(?, ?, ?, ?, ?, ?)', lottos)
conn.commit()
print("新增多筆資料成功")
conn.close()
