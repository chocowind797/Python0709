import tkinter as tk
from tkinter import ttk
import sqlite3


def add():
    sql = 'INSERT INTO student(name) VALUES("%s")' % var.get()
    cursor.execute(sql)
    conn.commit()
    query()
    var.set('')


def delete():
    sql = 'DELETE FROM student WHERE id = %s' % var.get()
    cursor.execute(sql)
    conn.commit()
    query()
    var.set('')


def query():
    cursor.execute('select id, name from student')
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

    win.title('Student')

    tree = ttk.Treeview(win, columns=['1', '2'], show='headings')  # 表格
    tree.heading('1', text='序號')
    tree.heading('2', text='姓名')

    tree.column('1', width=200, anchor='center')
    tree.column('2', width=200, anchor='center')

    query()

    my_frame = ttk.Frame(win)
    my_frame.pack()

    var = tk.StringVar()
    entry = tk.Entry(my_frame, textvariable=var, justify=tk.CENTER)

    addButton = tk.Button(my_frame, text='新增', command=add)

    queryButton = tk.Button(my_frame, text='查詢', command=query)

    delButton = tk.Button(my_frame, text='刪除', command=delete)

    entry.pack(side=tk.LEFT)
    addButton.pack(side=tk.LEFT)
    delButton.pack(side=tk.LEFT)
    queryButton.pack(side=tk.LEFT)
    tree.pack()

    temp = 0

    win.mainloop()
    conn.close()
