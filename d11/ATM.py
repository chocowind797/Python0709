class Account:
    __money = 0  # __var -> private var

    def __init__(self, money) -> None:  # __init__ -> 建構子
        self.__money = money

    def withdraw(self, x) -> None:
        print("提款: $" + str(x))
        if x <= 0:
            print("提款金額需大於0")
            return
        if x > self.__money:
            print("餘額不足")
            return
        self.__money -= x

    def save(self, x) -> None:
        print("存款: $" + str(x))
        if x <= 0:
            print("存款金額需大於0")
            return
        self.__money += x

    def __str__(self) -> str:
        return "帳戶餘額: " + str(self.__money)

    def transfer(self, target, money):
        print("\n轉帳給 %s 金額: $%d" % (target, money))
        if money > self.__money:
            print("餘額不足")
            return
        self.__money -= money
        print("轉帳成功")


if __name__ == '__main__':
    # account1 = Account(30000)
    # print(account1)
    # account1.withdraw(6000)
    # print(account1)
    # account1.withdraw(-6000)
    # print(account1)
    # account1.save(6000)
    # print(account1)

    account1 = Account(30000)
    account1.transfer("Mary", 3000)
    print(account1)
