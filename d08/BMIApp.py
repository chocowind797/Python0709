import d08.BubbleSort3 as bubble


def addBMI(datas):
    for data in datas:
        data.setdefault("bmi", "%.2f" % (data.get("w") / (data.get("h")/100)**2))
    return rows


if __name__ == '__main__':
    rows = [
        {"h": 170, "w": 60},
        {"h": 160, "w": 55},
        {"h": 180, "w": 70}]

    # bubble.sort("h", rows)
    # print(rows)
    # bubble.sort("h", rows)
    # print(rows)

    bubble.sort("bmi", addBMI(rows))
    print(rows)
