import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()

win.title("GUI 元件視窗")
win.geometry("300x300")

# GUI 元件配置
# 標籤 Label ===========================================================================================================
my_label = ttk.Label(win, text='我是標籤')
my_label.pack()

# 按鈕 Button ==========================================================================================================
my_button = ttk.Button(win, text='我是按鈕')
my_button.pack()

# 按鈕 Checkbutton =====================================================================================================
my_checkbutton = ttk.Checkbutton(win, text="同意")
my_checkbutton.pack()

# 窗框 Frame ===========================================================================================================
my_frame = ttk.Frame(win)
my_frame.pack()

# 按鈕 Radiobutton =====================================================================================================
m_radiobutton = ttk.Radiobutton(my_frame, text='男', value=1)  # 將 Radiobutton 放入 frame 內
f_radiobutton = ttk.Radiobutton(my_frame, text='女', value=2)  # 將 Radiobutton 放入 frame 內
m_radiobutton.pack(side=tk.LEFT)
f_radiobutton.pack(side=tk.LEFT)

# 輸入框 Entry =========================================================================================================
my_entry = ttk.Entry(win)
my_entry.pack()

# 下拉選單 =============================================================================================================
values = ['Python', 'Java', 'VB', 'C++']
my_combobox = ttk.Combobox(win, value=values)
my_combobox.pack()

win.mainloop()
