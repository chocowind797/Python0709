def getSum(scores):
    sum = 0
    for i in scores:
        sum += int(i)
    return sum


def getAvg(scores):
    return getSum(scores) / len(scores)


scores = input().split()
print("總分:", getSum(scores))
print("平均:", getAvg(scores))
