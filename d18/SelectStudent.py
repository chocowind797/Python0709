import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

print('序號 ', '身高\t', '體重\t\t', 'BMI\t\t', '姓名\t', sep='')
print("=================================")

sql = 'SELECT b.id, b.h, b.w, round(b.w/((b.h/100)*(b.h/100)), 2) as bmi, s.name ' \
      'FROM student as s, bmi as b ' \
      'WHERE s.id = b.sid ' \
      'GROUP BY name ' \
      'ORDER BY bmi'

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    for data in row:
        print(data, end='\t')
    print()
