class Account:
    __money = 0

    def __init__(self, money) -> None:
        self.__money = money

    def __str__(self) -> str:
        return "餘額為: $" + str(self.__money)

    def withdraw(self, money):
        print("提款: $" + str(money))
        if money > self.__money:
            print("餘額不足")
            return
        if money <= 0:
            print("提款金額需 > 0")
            return
        self.__money -= money

    def save(self, money):
        print("存款: $" + str(money))
        if money <= 0:
            print("提款金額需 > 0")
            return
        self.__money += money

    def transfer(self, targetAccount, money):
        print("轉帳: $" + str(money))
        if money > self.__money:
            print("餘額不足")
            return
        if money <= 0:
            print("轉帳金額需 > 0")
            return
        self.__money -= money
        targetAccount.__money += money
        print("轉帳成功")

    def getMoney(self):
        return self.__money
