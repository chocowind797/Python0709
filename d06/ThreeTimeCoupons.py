import requests
import json
url = "https://data.coa.gov.tw/Service/OpenData/DataFileService.aspx?UnitId=H54"

r = requests.get(url).text  # 取得網路原始字串資料

list = json.loads(r)  # 將 Json 字串轉成 Python 可用之物件

# rice = dict()

for data in list:
    name = data.get('特店對外名稱')
    print(name, data.get('特店網址'))
