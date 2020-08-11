def ham(func):
    print("我是火腿")
    return func


def onion(func):
    print("我是洋蔥")
    return func


def hotdog(func):
    print("我是熱狗")
    return func


@hotdog
@ham
@onion
def bread():
    print("我是麵包")


if __name__ == '__main__':
    bread()
