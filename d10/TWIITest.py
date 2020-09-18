import util.TWII as twii

rows = twii.analysys(10, 7, 1)
for row in rows:
    print(row)
print()
for data in twii.getProductByName('鴻海'):
    print(data)
