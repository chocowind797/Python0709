def usd(func):
    def inner(money):
        money /= 30
        return func(money)
    return inner


def jpy(func):
    def inner(money):
        money /= 0.28
        return func(money)
    return inner


@jpy
@usd
def exchange(money):
    print(money)


if __name__ == '__main__':
    exchange(30)
