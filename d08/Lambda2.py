if __name__ == '__main__':
    id = "A233334444"
    sex = id[1]
    dic = {
        "1": lambda: print("男"),
        "2": lambda: print("女")
    }
    dic.get(sex)()
