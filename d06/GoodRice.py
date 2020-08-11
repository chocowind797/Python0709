import requests
import json
url = "https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceQualified.aspx"

r = requests.get(url).text  # 取得網路原始字串資料

list = json.loads(r)  # 將 Json 字串轉成 Python 可用之物件

# rice = dict()

for data in list:
    name = data.get('品名')
    if name.__contains__('池上'):
        print(name, data.get('國際條碼'))
