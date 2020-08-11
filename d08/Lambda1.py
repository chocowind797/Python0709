def max(m, n):
    if m > n:
        return m
    return n


def max2(m, n):
    return m if m > n else n


if __name__ == '__main__':
    mymax = lambda m, n: m if m > n else n
    print(mymax(40, 60))
