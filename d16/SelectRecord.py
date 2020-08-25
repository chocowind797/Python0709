import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# 查詢 SQL
sql = 'select id, n1, n2, n3, n4, n5, n6, ts from lotto'

# 表格欄位名稱(Table Meta-info)
cursor.execute('pragma table_info({})'.format('lotto'))
metainfo = cursor.fetchall()
print("meta-info: ", metainfo)
names = [t[1] for t in metainfo]
print('names: ', names)
for name in names:
    print(name, end='\t')

print("\n===============================================")

cursor.execute(sql)
rows = cursor.fetchall()  # 以 list 型態回傳多筆資料
for row in rows:
    for data in row:
        print(data, end='\t')
    print()
conn.close()

print("===============================================")
print("\t\t\t  共有: %d 筆資料" % len(rows))
