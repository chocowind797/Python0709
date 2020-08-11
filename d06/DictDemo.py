fruits = {'orange': 20, 'apple': 10, 'watermelon': 30}

# get(key) 取得 value
print('orange 是', fruits.get('orange'))
print('apple 是', fruits.get('apple'))
print('watermelon 是', fruits.get('watermelon'))
print('banana 是', fruits.get('banana'))
print(fruits)

# setdefault(key, value) 若查無則新增
print('banana 是', fruits.setdefault('banana', 70))
print(fruits)
print('apple 是', fruits.setdefault('apple', 100))
print(fruits)

# keys() 取得所有 key
name = fruits.keys()
print(name, type(name))

# values() 取得所有 value
values = fruits.values()
print(values, type(values), sum(values))
