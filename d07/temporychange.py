def ctof(c) -> float:
    return c*9/5+32


def ftoc(f) -> float:
    return (f-32)*5/9


if __name__ == '__main__':
    mode = int(input("輸入華氏(1) 攝氏(2): "))
    temp = float(input("請輸入溫度: "))
    trans = ctof(temp) if mode == 2 else ftoc(temp)
    print("%.1f °%s ≈ %.1f °%s" % (temp, "F" if mode == 1 else "C", trans, "F" if mode == 2 else "C"))
