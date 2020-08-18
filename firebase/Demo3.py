import tkinter as tk
from firebase import firebase

firebase = firebase.FirebaseApplication('https://victor0816-b5ab4.firebaseio.com/', None)


def openTheDoor():
    while True:
        firebase.patch('/myhouse', {'open': 1})
        firebase.patch('/myhouse', {'open': 0})


def closeTheDoor():
    firebase.patch('/myhouse', {'open': 0})


win = tk.Tk()

win.title('Door Open')
win.geometry("300x110")

openButton = tk.Button(win, text='Open', command=openTheDoor, font=('Arial', 20))
openButton.pack(side=tk.LEFT)

closeButton = tk.Button(win, text='Close', command=closeTheDoor, font=('Arial', 20))
closeButton.pack(side=tk.RIGHT)

win.mainloop()
