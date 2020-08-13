import tkinter as tk

win = tk.Tk()

win.title("我的小視窗")
win.geometry("300x250")

label = tk.Label(win, text="Hello!")
label.pack()

win.mainloop()
