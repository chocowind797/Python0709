import sqlite3

sql = 'create table if not exists lotto(' \
      'id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
      'n1 INTEGER, ' \
      'n2 INTEGER, ' \
      'n3 INTEGER, ' \
      'n4 INTEGER, ' \
      'n5 INTEGER, ' \
      'n6 INTEGER, ' \
      'ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'

conn = sqlite3.connect('demo.db')  # 連線至demo.db資料庫
cursor = conn.cursor()  # 取得cursor指標(用來操作資料庫用)
cursor.execute(sql)  #
conn.commit()
print("建立完成")
conn.close()
