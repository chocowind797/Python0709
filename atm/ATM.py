import atm.Account as account
import os


def display():
    for act in actList:
        for key in act.keys():
            print(key, act.get(key))


def withdraw():
    actName = input("請輸入提款人: ").strip()
    money = int(input("請輸入提款金額: "))
    act = None
    for account in actList:
        for name in account.keys():
            if name == actName:
                act = account.get(name)
    if act is None:
        print("查無此人")
    else:
        act.save(money)


def save():
    actName = input("請輸入存款人: ").strip()
    money = int(input("請輸入存款金額: "))
    act = None
    for account in actList:
        for name in account.keys():
            if name == actName:
                act = account.get(name)

    if act is None:
        print("查無此人")
    else:
        act.save(money)


def transfer():
    actName = input("請輸入轉帳人(from): ").strip()
    actName_target = input("請輸入收款人(to): ").strip()
    money = int(input("請輸入轉帳金額: "))
    act = None
    act_target = None
    for account in actList:
        for name in account.keys():
            if name == actName:
                act = account.get(name)
            elif name == actName_target:
                act_target = account.get(name)
    if act is None or act_target is None:
        if act is None and act_target is None:
            print("查無" + actName + "和" + actName_target)
        elif act is None:
            print("查無" + actName)
        else:
            print("查無" + actName_target)
        print("轉帳失敗")
    else:
        act.transfer(act_target, money)


def createAccount():
    actName = input("輸入開戶人: ")
    money = int(input("初始金額: $"))
    act = account.Account(money)
    for actt in actList:
        for key in actt.keys():
            if actName == key:
                print("此帳戶已存在")
                return
    actList.append({actName: act})
    print(actName + "帳戶創建成功, 開戶金額: $" + str(money))


def cancelAccount():
    actName = input("請輸入解約人: ").strip()
    act = None
    for actt in actList:
        for key in actt.keys():
            if key == actName:
                act = actt
    if act is None:
        print("查無" + actName)
    else:
        actList.remove(act)
        print(actName + "解約成功, 解約金: $" + str(act.get(actName).getMoney()))


if __name__ == '__main__':
    act1 = account.Account(1000)
    act2 = account.Account(1000)
    act3 = account.Account(1000)

    actList = [{'John': act1}, {'Mary': act2}, {'Tom': act3}]

    while True:
        print('系統選單:')
        print('===========')
        print('1. 查詢')
        print('2. 存款')
        print('3. 提款')
        print('4. 轉帳')
        print('5. 開戶')
        print('6. 解約')
        print('9. 離開')
        print('===========')
        no = int(input("請選擇(1~9): "))
        print('===========')

        if no == 1:
            display()
        elif no == 2:
            save()
        elif no == 3:
            withdraw()
        elif no == 4:
            transfer()
        elif no == 5:
            createAccount()
        elif no == 6:
            cancelAccount()
        elif no == 9:
            break

        os.system('pause')
print("程式結束")
