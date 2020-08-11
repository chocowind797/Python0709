import random

while True:
    r = random.randint(1, 100)
    if r % 3 == 0:
        print(r)
        continue
    if r % 11 == 0:
        break
