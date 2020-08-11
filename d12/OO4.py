class BMI:
    h = 0
    w = 0
    name = ""
    __bmi = 0

    def __init__(self, name, h, w) -> None:
        self.name = name
        self.h = h
        self.w = w
        self.__bmi = w / (h / 100) ** 2

    def getBMI(self):
        return self.__bmi

    def __str__(self) -> str:
        return "%s h: %d w: %d bmi: %.2f" % (self.name, self.h, self.w, self.__bmi)


if __name__ == '__main__':
    file = open('student.txt', 'r')
    BMIlist = []
    for student in file.readlines():
        rows = student.split(", ")
        name = rows[0].strip()
        h = float(rows[1].strip())
        w = float(rows[2].strip())
        b = BMI(name, h, w)
        print(b)
        BMIlist.append(b)

    for bmi in BMIlist:
        print(bmi)
