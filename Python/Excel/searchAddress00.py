import openpyxl,os,sys
from openpyxl.utils import get_column_letter, column_index_from_string

import json
from urllib.request import urlopen, quote

def searchCoordinateByCommunityName(communityName):
    # url = 'http://api.map.baidu.com/geocoder/v2/'
    url = 'http://api.map.baidu.com/geocoder/v2/'

    output = 'json'
    ak = 'XXXXXXXXXXXXXXX'
    add = quote(communityName) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    ppp = 'kkkkkkkk'
    try:
        var= temp['result']['precise']
        # 判断是否为精确地址
        if var == 1:
            ppp = temp['result']['location']
        else:
            ppp = "1234567890 " + str(temp)
    except Exception as e:
        ppp = "1234567890 " + str(temp)
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
         Coordinate = searchCoordinateByCommunityName(cellObj.value)
         print(cellObj.coordinate, cellObj.value,Coordinate)
         address.append(Coordinate)
print(address)

array = [];
kkkkk = 0
for index in range(2,483):
   dic = address[index - 2]
   resttttt = ""
   try:
       status = dic["status"]
       print(status)
       if  status is 0:
           type1 =  dic["result"]["level"]
           print(type1)
           # 如果 level 的级别为 地产小区 就认为它是正确的数据
           if type1 is "地产小区":
               print("iiiiiiiii   " + type1)
               lng = dic["result"]["location"]['lng']
               lat = dic["result"]["location"]['lat']
               resttttt = "{'lng':%f,'lat':%f}" %(lng,lat)
               resttttt = "{'lng':%f,'lat':%f}" %(lng,lat)
           else:
               kkkkk += 1
               resttttt = "1111111" + str(dic)
       else:
            lng = dic['lng']
            lat = dic['lat']
            resttttt = "{'lng':%f,'lat':%f}" %(lng,lat)
            # resttttt = "{'lat':%f,'lng':%f}" %(lat,lng)

   except Exception as e:
       resttttt = dic
   array.append(resttttt)

print(array)
print("mmmmmmmmmmmmmm %d"%(kkkkk))
for index in range(2,483):
    try:
        # 写数据到对应的位置
        sheet["D%d" % (index)].value = str(array[index - 2])
    except Exception as e:
        dic = array[index - 2]
        print(index)
        print(type(dic))
        print(dic)
        print(dic["result"]["location"])
        sheet["D%d" % (index)].value = "222222222222"


wb.save('保存一个新的excel00001.xlsx')
