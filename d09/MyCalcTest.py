import util.MyCalc as calc
from util.MyCalc import bmi

if __name__ == '__main__':
    a = 10
    b = 20
    w = 60
    h = 170

    print(calc.sub(a, b))
    print(calc.add(a, b))

    print(bmi(h, w))
