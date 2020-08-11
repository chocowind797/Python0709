def calc(x=1, y=2) -> int:
    return x + y


def calc2(x=None, y=None) -> int:
    flag = False
    if x is None:
        print("使用者沒帶入x值")
        flag = True
    if y is None:
        print("使用者沒帶入y值")
        flag = True
    if flag:
        return 0
    return x + y


if __name__ == "__main__":
    sum = calc(10, 20)
    print(sum)
    sum = calc()
    print(sum)
    sum = calc(7)
    print(sum)
    sum = calc(y=7)
    print(sum)

    sum = calc2(6)
    print(sum)
    sum = calc2(y=7)
    print(sum)
    sum = calc2()
    print(sum)
    sum = calc2(10, 20)
    print(sum)
