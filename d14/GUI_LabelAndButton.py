import tkinter as tk

win = tk.Tk()

win.title("我的小視窗")
win.geometry("300x250")

label = tk.Label(win, text="Hello!")
label.pack()

button1 = tk.Button(win, text='OK')
button1.pack(side=tk.LEFT)

button2 = tk.Button(win, text='Exit')
button2.pack(side=tk.RIGHT)

win.mainloop()
