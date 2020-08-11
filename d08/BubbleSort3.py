def sort(key, rows):
    for i in range(len(rows) - 1, 0, -1):
        for j in range(i):
            if rows[j].get(key) > rows[j + 1].get(key):
                rows[j], rows[j + 1] = rows[j + 1], rows[j]


if __name__ == '__main__':

    rows = [{"age": 10, "score": 90},
            {"age": 40, "score": 100},
            {"age": 20, "score": 80}]

    sort("age", rows)
    print(rows)
