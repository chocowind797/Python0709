users = [
    {'name': 'John', 'height': 170, 'weight': 60},
    {'name': 'Mary', 'height': 160, 'weight': 48}
]

for user in users:
    name = user.get('name')
    height = user.get('height')
    weight = user.get('weight')

    bmi = "%.2f" % (weight / (height/100)**2)
    print(name, height, weight, " BMI \u2248", bmi)
