data = 'orange=10;apple=30;berry=20;banana=15'

# 與 todo1 if (condition) else todo2 相同邏輯
fruits = dict(item.split("=") for item in data.split(";"))

print(fruits)
