import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()

win.title("Button 布局")
# win.geometry("")

s = ttk.Style()
s.configure('My.TButton', font=('Arial', 15))

btn1 = ttk.Button(win, text='btn1', style='My.TButton')
btn2 = ttk.Button(win, text='btn2', style='My.TButton')
btn3 = ttk.Button(win, text='btn3', style='My.TButton')
btn4 = ttk.Button(win, text='btn4', style='My.TButton')
btn5 = ttk.Button(win, text='btn5', style='My.TButton')
btn6 = ttk.Button(win, text='btn6', style='My.TButton')

win.rowconfigure((0, 1), weight=1)
win.columnconfigure((0, 1, 2, 3), weight=1)

btn1.grid(row=0, column=0, columnspan=1, sticky="EWNS")
btn2.grid(row=0, column=1, columnspan=2, sticky="EWNS")
btn3.grid(row=0, column=3, rowspan=2,    sticky="EWNS")
btn4.grid(row=1, column=0, columnspan=1, sticky="EWNS")
btn5.grid(row=1, column=1, columnspan=1, sticky="EWNS")
btn6.grid(row=1, column=2, columnspan=1, sticky="EWNS")

win.mainloop()
