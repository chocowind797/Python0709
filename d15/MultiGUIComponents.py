import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()

win.title("GUI 元件視窗")
win.geometry("300x300")

# GUI 元件配置
# 標籤 Label
my_label = ttk.Label(win, text='我是標籤')
my_label.pack()

# 按鈕 Button
my_button = ttk.Button(win, text='我是按鈕')
my_button.pack()

# 按鈕 Checkbutton
my_checkbutton = ttk.Checkbutton(win, text="同意")
my_checkbutton.pack()

# 按鈕 Radiobutton
m_radiobutton = ttk.Radiobutton(win, text='男', value=1)
f_radiobutton = ttk.Radiobutton(win, text='女', value=2)
m_radiobutton.pack()
f_radiobutton.pack()

# 輸入框 Entry
my_entry = ttk.Entry(win)
my_entry.pack()

# 下拉選單
values = ['Python', 'Java', 'VB', 'C++']
my_combobox = ttk.Combobox(win, value=values)
my_combobox.pack()


win.mainloop()
