import requests
from lxml import etree
import json
import openpyxl
import urllib.request
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
res = requests.get(url=url).text
html = etree.HTML(res)
with open("data.html","wb") as f:
    f.write(response.read())
json_text = html.xpath('//script[@type="application/json"]/text()')
json_text = json_text[0]
result = json.loads(json_text)
result = result[0]['caseList']
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "国内疫情"
ws.append(["疫情地区","累计","治愈","死亡"])
for line in result:
    line_name = [line["area"],line["confirmed"],line["crued"],line["died"]]
    for ele in line_name:
        if ele == '':
            ele = 0
    ws.append(line_name)
wb.save('./china.xlsx')
