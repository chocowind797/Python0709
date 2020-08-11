from random import randint

lotto = set()
lotto2 = list()

while len(lotto) < 5:
    r = randint(1, 5)
    lotto.add(r)
    lotto2.append(r)
print(lotto)

print(lotto2)
lotto2 = tuple(lotto2)
print(lotto2)
