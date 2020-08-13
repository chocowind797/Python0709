class LoginException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return "登入錯誤, 原因: " + self.msg


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
        raise LoginException("無此帳號")
    if not check[1]:
        raise LoginException("密碼錯誤")
    return "登入成功"


if __name__ == '__main__':
    try:
        result = loginCheck('admin', '1234')
    except LoginException as le:
        print(le)
    else:
        print(result)
