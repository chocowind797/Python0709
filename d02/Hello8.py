pen = 15
amount = 200
total = pen * amount
print(pen, amount, total)
print(pen, amount, total, sep= '&')
print(pen, amount, total, sep= ',')
print('鉛筆每枝 ' + str(pen) + ' 元, ' + str(amount) + ' 枝總共 ' + str(total) + ' 元')
print('鉛筆每枝 %d 元, %d 枝總共 %d 元' % (pen, amount, total))
print('鉛筆每枝 {} 元, {} 枝總共 {} 元'.format(pen, amount, total))
