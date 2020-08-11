import statistics
import random as r

a = []
b = []

for i in range(10):
    a.append(r.randint(0, 10))
    b.append(r.randint(0, 10))


def getStat(list):
    list.sort()
    mean = statistics.mean(list)
    stdev = statistics.stdev(list)
    cv = stdev / mean

    return mean, stdev, cv


print(a)
print(b)

stat_a = getStat(a)
stat_b = getStat(b)

print(stat_a)
print(stat_b)
