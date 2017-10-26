# -*- coding: UTF-8 -*-
import requests, sys, webbrowser, bs4
import sys

#伪装浏览器头
def camouflageWrowser():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    return headers

# 读取输入参数并组装为搜索用的参数
def readInputParameterAndFormat():
    searchWorld =  ' '.join(sys.argv[1:])
    payload = {'wd':u'%s'%searchWorld}
    print("searchWorld = " + searchWorld)
    return  payload

# 搜索关键字
def requestsWithParameter(headers,parameter):
    url = 'http://www.baidu.com/s'
    r = requests.get(url, params=parameter, headers=headers, timeout=5)
    return r

# 查找需要的内容
def findNeedResult(request):
    # 查找需要的内容
    soup = bs4.BeautifulSoup(request.text,"html.parser")
    linkElems = soup.select('.result > .t > a[href]')
    topLinkElems = soup.select('.result-op > .t > a[href]')
    return linkElems + topLinkElems

# 打开全部搜索结果
def openElement(el):
    webbrowser.open(el.get('href'))


#伪装浏览器头
headers = camouflageWrowser()
# 读取输入参数
payload = readInputParameterAndFormat()
# 请求关键字数据
r = requestsWithParameter(headers,payload)
# 解析返回的结果
linkElems =  findNeedResult(r)

for el in linkElems:
    openElement(el)
