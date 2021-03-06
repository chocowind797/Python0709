import sqlite3
import sys


conn = sqlite3.connect('school.db')


def menu():
    print("===============================================")
    print('1.建立表單')
    print('2.新增紀錄')
    print('3.全部查詢')
    print('4.單筆查詢')
    print('5.修改紀錄')
    print('6.刪除紀錄')
    print('7.清除紀錄')
    print('9.離開系統')
    print("===============================================")
    n = int(input("請選擇: "))
    print("===============================================")
    if n == 9:
        return
    else:
        choice(n)
    print('按下 Enter 鍵繼續...', end='')
    sys.stdin.read(1)
    menu()


def choice(n):
    {
        1: lambda: createTable(),
        2: lambda: insertRecord(),
        3: lambda: selectAllRecord(),
        4: lambda: selectRecord(),
        5: lambda: updateRecord(),
        6: lambda: deleteRecord(),
        7: lambda: deleteAllRecord()
    }[n]()


def createTable():
    try:
        sql = open('data.sql', 'r').read()
        conn.execute(sql)
        conn.commit()
        print("資料表建立完成")
    except sqlite3.OperationalError:
        print("資料表已存在!!")


def insertRecord():
    name = input("請輸入姓名: ")
    age = int(input("請輸入年齡: "))
    sex = int(input("請輸入性別(1:男, 2.女): "))
    sql = "insert into student(name, age, sex) values('%s', %d, %d)" % (name, age, sex)
    cursor = conn.execute(sql)
    print('新增成功, id=', cursor.lastrowid)
    conn.commit()


def selectAllRecord():
    cursor = conn.cursor()
    cursor.execute('pragma table_info({})'.format('lotto'))
    metainfo = cursor.fetchall()
    names = [t[1] for t in metainfo]
    for name in names:
        print(name, end='\t')

    print("\n===============================================")
    sql = 'select * from student'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        for data in row:
            print(data, end="\t")
        print()


def selectRecord():
    name = input('請輸入要查詢的人名: ')
    sql = 'select * from student where name="%s"' % name
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("查無此人")
    for row in rows:
        for data in row:
            print(data, end="\t")
        print()


def updateRecord():
    id = int(input('請輸入要修改的id號碼: '))
    flag = input('是否要修改姓名?(y/n): ')
    if flag == 'y':
        name = input('請輸入姓名: ')
        sql = 'update student SET name = "%s" WHERE id = %d' % (name, id)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print('修改姓名成功!')

    flag = input('是否要修改年齡?(y/n): ')
    if flag == 'y':
        age = int(input('請輸入年齡: '))
        sql = 'update student SET age = %d WHERE id = %d' % (age, id)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print('修改年齡成功!')

    flag = input('是否要修改性別?(y/n): ')
    if flag == 'y':
        sex = int(input('請輸入性別: '))
        sql = 'update student SET sex = %d WHERE id = %d' % (sex, id)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print('修改性別成功!')


def deleteRecord():
    id = int(input('請輸入要刪除的id號碼: '))
    sql = 'delete from student WHERE id = %d' % id
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(id, ' 紀錄刪除成功!')


def deleteAllRecord():
    sql = 'delete from student'
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(' 紀錄清除成功!')


if __name__ == '__main__':
    menu()
    conn.close()
