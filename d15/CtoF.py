import tkinter as tk
import tkinter.ttk as ttk

global string_c
global string_f


def ctof():
    try:
        c = string_c.get()
        if c == '':
            c = 0
            string_c.set("0")
        c = "%.1f" % (float(c) * 9 / 5 + 32)
        string_f.set(c)
    except ValueError:
        string_c.set("輸入錯誤")


def ftoc():
    try:
        f = string_f.get()
        if f == '':
            f = 0
            string_f.set("0")
        f = "%.1f" % ((float(f) - 32) * 5 / 9)
        string_c.set(f)
    except ValueError:
        string_f.set("輸入錯誤")


def clear():
    string_c.set("")
    string_f.set("")


win = tk.Tk()

win.title("華氏/攝氏轉換")
win.geometry("300x100")

frame_c = tk.Frame(win)
frame_f = tk.Frame(win)
frame_c.pack()
frame_f.pack()

# 攝氏
label_c = ttk.Label(frame_c, text='攝氏', font=('Arial', 20))

string_c = tk.StringVar()
entry_c = tk.Entry(frame_c, textvariable=string_c, justify="center")

button_c = ttk.Button(frame_c, text='轉換', style="My.TButton", command=ctof)

label_c.pack(side=tk.LEFT)
entry_c.pack(side=tk.LEFT)
button_c.pack(side=tk.LEFT)

# 華氏
label_f = ttk.Label(frame_f, text='華氏', font=('Arial', 20))

string_f = tk.StringVar()
entry_f = tk.Entry(frame_f, textvariable=string_f, justify="center")

button_f = ttk.Button(frame_f, text='轉換', style="My.TButton", command=ftoc)

label_f.pack(side=tk.LEFT)
entry_f.pack(side=tk.LEFT)
button_f.pack(side=tk.LEFT)

# 清除
button_clear = ttk.Button(win, text='清除', style="My.TButton", command=clear)
button_clear.pack()

win.mainloop()
