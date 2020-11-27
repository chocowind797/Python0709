import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msg


# ===================================backspace=====================================


def reset():
    global isEqual
    global isPoint
    isEqual = False
    isPoint = False


def clear():
    ans.set("")
    reset()


def back():
    a = ans.get()
    if a[len(a) - 1] == ' ':
        a = a[:len(a) - 3]
    else:
        pos = a[len(a) - 1]
        if pos == '.':
            global isPoint
            isPoint = False
        a = a[:len(a) - 1]
    ans.set(a)


# ====================================number=====================================


def checkEqual():
    global isEqual
    if isEqual:
        isEqual = False
        ans.set("")


def checkZero():
    if len(ans.get()) == 0 or isPoint:
        return True
    if not ans.get().__contains__(" "):
        if ans.get()[0] == '0':
            return "replace"
        return True
    symbolList = ['+', '-', '*', '/']
    index = []
    for symbol in symbolList:
        index.append(ans.get().rfind(symbol))
    i = max(index)
    a = ans.get()[i + 1:]

    def checkagain(a):
        if len(a) == 0 or isPoint:
            return True
        if a[0] == '0':
            return "replace"
        return True

    a = a.replace(' ', '')
    return checkagain(a)


def number(num):
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + num)
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + num)
        return
    ans.set(ans.get() + num)
    

def m0():
    checkEqual()
    if len(ans.get()) == 0:
        ans.set(ans.get() + "0")
        return
    if not ans.get().__contains__(" "):
        if ans.get()[0] != '0' or isPoint:
            ans.set(ans.get() + "0")
            return
    symbolList = ['+', '-', '*', '/']
    index = []
    for symbol in symbolList:
        index.append(ans.get().rfind(symbol))
    i = max(index)
    a = ans.get()[i + 1:]

    def m0_1(a):
        if len(a.replace(' ', '')) == 0:
            a = a + "0"
            return a
        if a.replace(' ', '')[0] != '0' or isPoint:
            a = a + "0"
            return a
    if m0_1(a) is None:
        return
    ans.set(ans.get()[:i + 1] + m0_1(a))

# ===================================symbol=====================================


def checkSymbol():
    a = ans.get()
    if a == '':
        return None
    elif a[len(a) - 1] == '.':
        ans.set(a[:len(a)-1])
        return True
    elif not a[len(a) - 2].isdigit() and a[len(a) - 2] != '.' and a[len(a) - 2] != ' ':
        return "replace"
    else:
        return True


def checkSymbolEqual():
    global isEqual
    if isEqual:
        isEqual = False


def symbol(symbol):
    global isPoint
    check = checkSymbol()
    if check is None:
        ans.set("")
    elif symbol == 'replace':
        print("replace")
        ans.set(ans.get()[:len(ans.get()) - 3] + symbol)
    else:
        ans.set(ans.get() + symbol)
    checkSymbolEqual()
    isPoint = False
    

def equal():
    global isEqual
    global isPoint
    a = ans.get()
    if a == '':
        ans.set("0")
        isEqual = True
    elif not a[len(a) - 1].isdigit():
        if a[len(a) - 1] == '.':
            ans.set(a[:len(a)-1])
            equal()
            return
        msg.showerror('錯誤', '輸入函式錯誤')
    elif not a.isdigit():
        global records
        a = eval(ans.get().replace(' ', ''))
        if a is float:
            a = "%.2f" % a
            checkExist(ans.get() + " = " + a)
            ans.set(a)
        else:
            checkExist(ans.get() + " = " + str(a))
            ans.set(a)
        isEqual = True
        isPoint = False


def point():
    a = ans.get()
    global isPoint
    if not isPoint:
        if ans.get() == '' or not a[len(a) - 1].isdigit():
            ans.set(ans.get() + "0.")
        else:
            ans.set(ans.get() + ".")
        isPoint = True


# ===================================function====================================

def checkExist(string):
    global records
    if records.__contains__(string):
        return
    records.append(string)
    

def show():
    '''global isShow
    if isShow:
        record_combobox.grid_forget()
        isShow = False
    else:
        record_combobox.grid(row=0, column=4, rowspan=5, sticky="EWN")
        isShow = True'''

    def fill(event):
        string = record_combobox.get()
        index = str(string).index('=')
        string = string[:index - 1]
        ans.set(string)
        
    record = tk.Toplevel(win)
    record.title('紀錄')
    record.geometry('160x100')

    record_combobox = ttk.Combobox(record, value=records, state='readonly', height=5)
    record_combobox.bind("<<ComboboxSelected>>", fill)
    record_combobox['value'] = records
    
    record_combobox.pack()
    

if __name__ == '__main__':
    win = tk.Tk()

    win.title("計算機")
    win.geometry("500x400")
    win.config(bg='#D3D3D3')

    f = ("Arial", 20)

    # Button
    btn_clear = tk.Button(win, text='C', font=f, command=clear, bg='gray', fg='white')
    btn_back = tk.Button(win, text='<-', font=f, command=back, bg='gray', fg='white')
    btn_div = tk.Button(win, text='/', font=f, command=lambda : symbol(' / '), bg='gray', fg='white')
    btn_7 = tk.Button(win, text='7', font=f, command=lambda : number('7'), bg='black', fg='white')
    btn_8 = tk.Button(win, text='8', font=f, command=lambda : number('8'), bg='black', fg='white')
    btn_9 = tk.Button(win, text='9', font=f, command=lambda : number('9'), bg='black', fg='white')
    btn_time = tk.Button(win, text='*', font=f, command=lambda : symbol(' * '), bg='gray', fg='white')
    btn_4 = tk.Button(win, text='4', font=f, command=lambda : number('4'), bg='black', fg='white')
    btn_5 = tk.Button(win, text='5', font=f, command=lambda : number('5'), bg='black', fg='white')
    btn_6 = tk.Button(win, text='6', font=f, command=lambda : number('6'), bg='black', fg='white')
    btn_minus = tk.Button(win, text='-', font=f, command=lambda : symbol(' - '), bg='gray', fg='white')
    btn_1 = tk.Button(win, text='1', font=f, command=lambda : number('1'), bg='black', fg='white')
    btn_2 = tk.Button(win, text='2', font=f, command=lambda : number('2'), bg='black', fg='white')
    btn_3 = tk.Button(win, text='3', font=f, command=lambda : number('3'), bg='black', fg='white')
    btn_add = tk.Button(win, text='+', font=f, command=lambda : symbol(' + '), bg='gray', fg='white')
    btn_0 = tk.Button(win, text='0', font=f, command=m0, bg='black', fg='white')
    btn_point = tk.Button(win, text='.', font=f, command=point, bg='black', fg='white')
    btn_equ = tk.Button(win, text='=', font=f, command=equal, bg='gray', fg='white')
    #btn_record = tk.Button(win, text='紀錄', font=("Arial", 15), command=show, bg='gray', fg='white')
    
    # Menu
    record = tk.Menu(win)
    record.add_command(label='紀錄', command=show)
    
    # Label
    ans = tk.StringVar()
    label_ans = ttk.Label(win, textvariable=ans, font=("Arial", 22), anchor=tk.E)

    # Combobox
    records = []
    '''record_combobox = ttk.Combobox(win, value=records, state='readonly', height=5)
    record_combobox.bind("<<ComboboxSelected>>", fill)
    '''
    # put in

    win.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    win.columnconfigure((0, 1, 2, 3), weight=1)

    col_count, row_count = win.grid_size()

    label_ans.grid(row=0, column=0, columnspan=4, sticky="EWNS")
    btn_clear.grid(row=1, column=0, columnspan=2, sticky="EWNS", padx=1, pady=1)
    btn_back.grid(row=1, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_div.grid(row=1, column=3, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_7.grid(row=2, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_8.grid(row=2, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_9.grid(row=2, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_time.grid(row=2, column=3, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_4.grid(row=3, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_5.grid(row=3, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_6.grid(row=3, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_minus.grid(row=3, column=3, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_1.grid(row=4, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_2.grid(row=4, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_3.grid(row=4, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_add.grid(row=4, column=3, rowspan=2, sticky="EWNS", padx=1, pady=1)
    btn_0.grid(row=5, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_point.grid(row=5, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_equ.grid(row=5, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    #btn_record.grid(row=0, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    #record_combobox.grid(row=0, column=4, rowspan=5, sticky="EWN")
    win.config(menu=record)

    
    #record_combobox.grid_forget()

    # config
    isShow = False
    isEqual = False
    isPoint = False

    win.mainloop()
