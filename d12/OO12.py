class USD:
    def __get__(self, instance, owner):
        return instance.money / 30

    def __set__(self, instance, value):
        instance.money = value * 30


class JPY:
    def __get__(self, instance, owner):
        return instance.money / 0.28

    def __set__(self, instance, value):
        instance.money = value * 0.28


class CNY:
    def __get__(self, instance, owner):
        return instance.money / 5

    def __set__(self, instance, value):
        instance.money = value * 5


class Exchange:
    usd = USD()
    jpy = JPY()
    cny = CNY()

    def __init__(self, money) -> None:
        self.money = money

    def __str__(self) -> str:
        return str(self.money)


if __name__ == '__main__':
    ex = Exchange(10000)
    print(ex.usd)
    print(ex.jpy)
    print(ex.cny)
    ex.usd = 10
    print(ex)
    ex.cny = 30
    print(ex)
    ex.jpy = 60
    print(ex)
