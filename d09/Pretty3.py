def confirm(func):
    def inner(a, b):
        if b == 0:
            print("分母不可為0")
            return
        return func(a, b)
    return inner


@confirm
def div(a, b):
    return a / b


if __name__ == '__main__':
    print(div(10, 2))
    print(div(10, 0))
