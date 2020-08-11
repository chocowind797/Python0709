import requests
import json
from math import sin, asin, cos, radians, fabs, sqrt


def getUbikes() -> list:
    url = "https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=500"

    r = requests.get(url).text  # 取得網路原始字串資料

    return json.loads(r).get('result').get('records')  # 將 Json 字串轉成 Python 可用之物件


def getUbikeByName(sna, ubikes=None) -> dict:
    if ubikes is None:
        ubikes = getUbikes()
    for ubike in ubikes:
        if ubike.get('sna').__contains__(sna):
            return ubike


# 引用自 https://ixyzero.com/blog/archives/4238.html
def haversine(lon1, lat1, lon2, lat2) -> float:  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 將十進制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def near(distance, ubikes) -> list:
    all = []
    for ubike in ubikes:
        if ubike.get('distance') <= distance:
            all.append(ubike.get('sna'))
    return all


def appendDistance(lng, lat, ubikes) -> None:
    for ubike in ubikes:
        ubike.setdefault("distance", haversine(lng, lat, float(ubike.get('lng')), float(ubike.get('lat'))))


def lendBike(amount, ubikes) -> list:
    all = []
    dic = dict()
    for ubike in ubikes:
        if int(ubike.get('sbi')) >= amount:
            if dic.__contains__(ubike.get("distance")):
                dic[ubike.get("distance")] = [dic.get(ubike.get("distance"))].append(ubike.get("sna") + " %s/%s %.1fm" % (ubike.get('sbi'), ubike.get('tot'), ubike.get('distance')))
            else:
                dic.setdefault(ubike.get("distance"), [ubike.get("sna") + " %s/%s  %.1fm" % (ubike.get('sbi'), ubike.get('tot'), ubike.get('distance'))])

    keys = list(dic.keys())
    keys = sorted(keys)

    for key in keys:
        if len(dic.get(key)) > 1:
            for data in dic.get(key):
                all.append(data)
        else:
            all.append(dic.get(key))
    return all


def printLend(all, limit=None) -> None:
    if limit is None:
        limit = len(all)
    for datas in all:
        if limit > 0:
            limit -= 1
            for data in datas:
                if limit != 0:
                    print("[%s]" % data, end=", ")
                else:
                    print("[%s]" % data)


if __name__ == '__main__':
    lng = 121.311989
    lat = 24.990042
    distance = 500
    amount = 20
    limit = 5

    ubikes = getUbikes()
    appendDistance(lng, lat, ubikes)

    ubike = getUbikeByName('桃園火車站(前站)')
    near = near(distance, ubikes)
    lend = lendBike(amount, ubikes)

    print("%s 剩餘: %s/%s台" % (ubike.get('sna'), ubike.get('sbi'), ubike.get("tot")))
    print(near)
    printLend(lend, limit)
