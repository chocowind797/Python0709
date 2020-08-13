users = [{'name': "john", 'password': '4321'},
         {'name': "admin", 'password': '1234'}
         ]


def loginCheck(u, p):
    check = [False, False]
    for user in users:
        if user['name'] == u:
            check[0] = True
        if user['password'] == p:
            check[1] = True
    if not check[0]:
        raise Exception("查無此帳號")
    if not check[1]:
        raise Exception("密碼錯誤")
    return "登入成功"


if __name__ == '__main__':
    try:
        result = loginCheck('admin', '1234')
    except Exception as e:
        print(e)
    else:
        print(result)
