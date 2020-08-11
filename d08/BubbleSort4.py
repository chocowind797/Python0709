def sort(rows, reverse=False):
    for i in range(len(rows)-1, 0, -1):
        for j in range(i):
            if not reverse:
                if rows[j] > rows[j+1]:
                    rows[j], rows[j+1] = rows[j+1], rows[j]
            else:
                if rows[j] < rows[j+1]:
                    rows[j], rows[j+1] = rows[j+1], rows[j]


if __name__ == '__main__':
    rows = [8, 3, 5, 7, 2]
    sort(rows, reverse=True)
    print(rows)
