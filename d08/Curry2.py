def login(permission):
    def loginPass(money):
        return 100 if money > 100 else 100

    def loginFail(money):
        return 0

    return loginPass if permission == 'admin' else loginFail


if __name__ == '__main__':
    # 鞣製(要先..., 才能...)-
    # 先登入才能提錢
    print(login('admin')(100))
    print(login('hacker')(100))
