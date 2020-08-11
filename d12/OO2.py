class BMI:
    h = 0
    w = 0
    __bmi = 0

    def calcBMI(self) -> None:
        self.__bmi = self.w / (self.h / 100) ** 2

    def getBMI(self) -> float:
        return self.__bmi


if __name__ == '__main__':
    b = BMI()
    b.h = 170
    b.w = 60
    b.calcBMI()
    print("bmi \u2248 %.2f" % b.getBMI())
