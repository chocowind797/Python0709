def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def times(x, y):
    return x * y


def by(x, y):
    return x / y


def calc(func, x, y=1):
    if x < 200:
        x = 200
    return func(x, y)


if __name__ == '__main__':
    print(calc(add, 50))
    print(calc(add, 250))
    print(calc(minus, 70))
    print(calc(minus, 700))
