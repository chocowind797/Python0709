users = {'John': [170, 60], 'Mary': [160, 48]}
print(users)

names = users.keys()
for name in names:
    h = users.get(name)[0]
    w = users.get(name)[1]
    bmi = w / (h/100)**2
    print(name, users.get(name), "%.2f" % bmi)
