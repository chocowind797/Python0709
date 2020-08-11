import statistics
import random as r

scores = []

for i in range(10):
    scores.append(r.randint(0, 10))
scores.sort()

print(scores)

scores.__delitem__(0)
scores.__delitem__(0)


scores.__delitem__(len(scores)-1)
scores.__delitem__(len(scores)-1)


print(scores)

mean = statistics.mean(scores)
print("平均 \u2248 %.2f " % mean)

stdev = statistics.stdev(scores)
print("標準差 \u2248 %.2f" % stdev)

cv = stdev / mean
print("變異數 \u2248 %.2f" % cv)
