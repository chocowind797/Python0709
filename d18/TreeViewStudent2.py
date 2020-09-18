import tkinter as tk
from tkinter import ttk
import sqlite3


def add():
    sql = 'INSERT INTO bmi(h, w, sid) VALUES(%s, %s, %s)' % (h.get(), w.get(), sid.get())
    print(sql)
    cursor.execute(sql)
    print(cursor.lastrowid)
    conn.commit()
    query()
    sid.set('')
    h.set('')
    w.set('')


def delete():
    sql = 'DELETE FROM student WHERE id = %s' % sid.get()
    cursor.execute(sql)
    conn.commit()
    query()
    sid.set('')


def query():
    sql = 'select b.id, b.h, b.w, round(b.w/((b.h/100)*(b.h/100)), 2) as bmi, s.name, s.id ' \
          'FROM student as s, bmi as b ' \
          'WHERE s.id = b.sid ' \
          'ORDER BY bmi'
    cursor.execute(sql)
    for i in tree.get_children():
        tree.delete(i)
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)


if __name__ == '__main__':
    # =======================================================sql=======================================================
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    # =====================================================tkinter=====================================================
    win = tk.Tk()

    win.title('Bmi')

    tree = ttk.Treeview(win, columns=['1', '2', '3', '4', '5', '6'], show='headings')  # 表格
    tree.heading('1', text='序號')
    tree.heading('2', text='身高')
    tree.heading('3', text='體重')
    tree.heading('4', text='BMI')
    tree.heading('5', text='姓名')
    tree.heading('6', text='學號')

    tree.column('1', width=100, anchor='center')
    tree.column('2', width=100, anchor='center')
    tree.column('3', width=100, anchor='center')
    tree.column('4', width=100, anchor='center')
    tree.column('5', width=100, anchor='center')
    tree.column('6', width=100, anchor='center')

    query()

    frameE = ttk.Frame(win)
    frameE.pack()

    frameB = ttk.Frame(win)
    frameB.pack()

    sid = tk.StringVar()
    entry_sid = tk.Entry(frameE, textvariable=sid, justify=tk.CENTER)

    h = tk.StringVar()
    entry_h = tk.Entry(frameE, textvariable=h, justify=tk.CENTER)

    w = tk.StringVar()
    entry_w = tk.Entry(frameE, textvariable=w, justify=tk.CENTER)

    addButton = tk.Button(frameB, text='新增', command=add)

    queryButton = tk.Button(frameB, text='查詢', command=query)

    delButton = tk.Button(frameB, text='刪除', command=delete)

    label_sid = tk.Label(frameE, text='學號:', font=('Arial', 15))
    label_h = tk.Label(frameE, text='身高:', font=('Arial', 15))
    label_w = tk.Label(frameE, text='體重:', font=('Arial', 15))

    label_sid.grid(row=0, column=0)
    entry_sid.grid(row=0, column=1)

    label_h.grid(row=1, column=0)
    entry_h.grid(row=1, column=1)

    label_w.grid(row=2, column=0)
    entry_w.grid(row=2, column=1)

    addButton.pack(side=tk.LEFT)
    delButton.pack(side=tk.LEFT)
    queryButton.pack(side=tk.LEFT)
    tree.pack()

    temp = 0

    win.mainloop()
    conn.close()
