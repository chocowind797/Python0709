if __name__ == '__main__':
    exchange = {
        'usd': lambda twd: print(twd / 30),
        'jpy': lambda twd: print(twd * 4)
    }
    exchange['usd'](300)
    exchange['jpy'](300)
