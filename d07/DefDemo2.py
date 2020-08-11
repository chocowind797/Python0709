def calc(*score) -> int:
    print(type(score), score)
    sum = 0
    for i in score:
        sum += i
    return sum


if __name__ == '__main__':
    sum = calc(10, 20, 30, 40)
    print(sum)
    sum = calc()
    print(sum)
