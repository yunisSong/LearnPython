# -*- coding: UTF-8 -*-
import requests, sys, webbrowser, bs4,os

currentFilePath = sys.path[0]
webFilePath = os.path.join(currentFilePath, "file")
os.chdir(webFilePath)

url = 'http://xkcd.com' # starting url

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        playFile = open(os.path.basename(comicUrl), 'wb')
        # playFile = open('python000000.jpg', 'wb')

        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
