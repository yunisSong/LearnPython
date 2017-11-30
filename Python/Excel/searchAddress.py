import openpyxl,os,sys
from openpyxl.utils import get_column_letter, column_index_from_string

import json
from urllib.request import urlopen, quote

def searchCoordinateByCommunityName(communityName):
    # url = 'http://api.map.baidu.com/geocoder/v2/'
    url = 'http://api.map.baidu.com/geocoder/v2/'

    output = 'json'
    ak = 'xxxxxxxxxxxxxxxxxxxxxxxx'
    add = quote(communityName) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    try:
        ppp = temp['result']['location']
    except Exception as e:
        ppp = temp
    return ppp

# 进入同级目录下的file文件夹
currentFilePath = sys.path[0]
webFilePath = os.path.join(currentFilePath, "doc")
os.chdir(webFilePath)

wb = openpyxl.load_workbook('python.xlsx')
# 获取所有表名的列表
print(wb.get_sheet_names())
# 根据名字获取列表
sheet = wb.get_sheet_by_name('Yunis000')
 address = []
 for rowOfCellObjects in sheet['C2':'C482']:
     for cellObj in rowOfCellObjects:
         # print(type(cellObj),type(rowOfCellObjects))
         Coordinate = searchCoordinateByCommunityName(cellObj.value)
         print(cellObj.coordinate, cellObj.value,Coordinate)
         address.append(Coordinate)

 print(address)

array = [];
for index in range(2,483):
    dic = address[index - 2]
    print(type(dic))
    print(dic)
    try:
        lng = dic['lng']
        lat = dic['lat']
        str = "{'lng':%f,'lat':%f}" %(lng,lat)
    except Exception as e:
        str = "Error"
    array.append(str)

print(array)

 for index in range(2,483):
   sheet["D%d" % (index)].value = str(address[index - 2])

wb.save('保存一个新的excel.xlsx')
