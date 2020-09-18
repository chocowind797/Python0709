import requests
import json
url = "https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx"

r = requests.get(url).text  # 取得網路原始字串資料

list = json.loads(r)  # 將 Json 字串轉成 Python 可用之物件

# rice = dict()

for data in list:
    if data.get('品名').__contains__("台稉"):
        # rice.setdefault(data.pop('品名'), data.get('不合格原因'))
        print(data.get('品名'), data.get('不合格原因'))
# print(rice)
