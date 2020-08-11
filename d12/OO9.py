class Number:
    def __init__(self, n) -> None:
        self.n = n

    def __str__(self) -> str:
        return str(self.n)

    def __pow__(self, power, modulo=None):
        self.n **= power
        return self.n


if __name__ == '__main__':
    n = Number(4)
    print(n ** 8)
