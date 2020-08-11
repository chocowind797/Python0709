import math

a = input("輸入a點座標: ").split(", ")
b = input("輸入b點座標: ").split(", ")

d = math.sqrt((int(a[0]) + int(b[0]))**2 + (int(a[1]) + int(b[1]))**2)

result = "a點座標({}, {}) 與 b點座標({}, {}) 的直線距離 {:.2f}".format(a[0],a[1],b[0],b[1], d)

print(result)
