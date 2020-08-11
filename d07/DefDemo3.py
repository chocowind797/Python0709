def calc(id, no, *score, **info):
    print(type(score), type(info))
    print('%d號. 姓名: %s  學號: %d  年齡: %d  總分: %d' % (
        no, info.get('name'), id, info.get('age'), sum(score)
    ))


if __name__ == '__main__':
    calc(810704, 24, 50, 60, 70, 80, 90, name='Victor', age=16)
