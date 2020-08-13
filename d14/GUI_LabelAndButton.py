import tkinter as tk
from tkinter import messagebox


def hello():
    messagebox.showinfo('Hello', 'Python')


def cancel():
    win.quit()


win = tk.Tk()

win.title("我的小視窗")
win.geometry("300x250")

label = tk.Label(win, text="Hello!")
label.config(font=('Arial', 40), bg='red', fg='yellow')
label.pack()

button1 = tk.Button(win, text='OK', command=hello)
button1.config(font=("Arial", 30))
button1.pack(side=tk.LEFT)

button2 = tk.Button(win, text='Exit', command=cancel)
button2.config(font=("Arial", 30))
button2.pack(side=tk.RIGHT)

win.mainloop()
