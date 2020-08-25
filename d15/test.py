import tkinter as tk
from tkinter import ttk

tkwindow = tk.Tk()

cbox = ttk.Combobox(tkwindow, values=[1, 2, 3], state='readonly')
cbox.grid(column=0, row=0)


def callback(eventObject):
    print(cbox.get())


cbox.bind("<<ComboboxSelected>>", callback)

tkwindow.mainloop()
