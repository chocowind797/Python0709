if __name__ == '__main__':
    level = ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'C', 'B', 'A', 'A']
    dic = {
        "level": lambda score: print(level[score//10])
    }
    dic.get('level')(95)
    dic.get('level')(85)
    dic.get('level')(75)
    dic.get('level')(65)
    dic.get('level')(55)
    dic.get('level')(25)
