def calc(amount, legs):
    rabbit = legs / 2 - amount
    chicken = amount - rabbit

    rabbit2 = (legs - 2 * amount) / 2
    chicken2 = amount - rabbit2

    return rabbit, chicken, rabbit2, chicken2


amount = int(input("::: "))
legs = int(input("::: "))

if legs/4 <= amount <= legs/2:

    result = calc(amount, legs)

    print("兔子:%d 雞:%d" % (result[0], result[1]))
    print(4*result[0] + 2*result[1])

    '''
    r + (83-r) = 83
    4r + 2(83-r) = 240
    4r = 240 - 2(83-r)
    2r = 120 - 83 + r
    r = 120 - 83
    '''

    print("兔子:%d 雞:%d" % (result[2], result[3]))
    print(4*result[2] + 2*result[3])

    '''
    2*83 = 166
    240 - 166 = 74
    74 / 2 = r
    83 - r = c
    '''
else:
    print("數值錯誤\t無法計算")
