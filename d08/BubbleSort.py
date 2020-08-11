rows = [8, 3, 5, 7, 2]

for i in range(len(rows)-1, 0, -1):
    for j in range(i):
        if rows[j] > rows[j+1]:
            rows[j], rows[j+1] = rows[j+1], rows[j]
        print(rows)

print("===============")

rows = [8, 3, 5, 7, 2]
for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        if rows[i] > rows[j]:
            rows[i], rows[j] = rows[j], rows[i]
        print(rows)
# print(rows)
