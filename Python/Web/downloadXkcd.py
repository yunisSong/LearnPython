# -*- coding: UTF-8 -*-
import requests, sys, webbrowser, bs4,os

# 进入同级目录下的file文件夹
currentFilePath = sys.path[0]
webFilePath = os.path.join(currentFilePath, "file")
os.chdir(webFilePath)

url = 'http://xkcd.com' # starting url
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    # 下载 网页
    res = requests.get(url)
    res.raise_for_status()
    # 解析查找需要的内容
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        # 拼接真实的图片下载地址
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # 保存图片到本地
        playFile = open(os.path.basename(comicUrl), 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()
        # 设置下一个加载的 链接
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
