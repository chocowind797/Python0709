import random


def check():
    r = random.randint(1, 9)
    print(r)
    return True if r % 2 == 0 else False


while check():
    print("Python")
