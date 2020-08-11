def isPrime(num):
    if num == 2:
        return True
    for n in range(2, num//2+1):
        if num % n == 0:
            return False
    return True


if '__main__' == __name__:  # Python主程式
    i = int(input(""))
    print(i, " 是" if isPrime(i) else " 不是", "質數", sep="")
