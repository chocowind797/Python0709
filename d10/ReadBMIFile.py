file = open('bmi.csv', 'r')
data = file.read()
print(type(data))
print(data)

file = open('bmi.csv', 'r')
data = file.readlines()

print(type(data))
print(data)
