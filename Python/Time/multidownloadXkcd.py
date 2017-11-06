# -*- coding: UTF-8 -*-
import requests, sys, webbrowser, bs4,os,threading

# 进入同级目录下的file文件夹
currentFilePath = sys.path[0]
os.chdir(currentFilePath)
os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))

        res = requests.get('http://xkcd.com/%s' % (urlNumber))

        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            comicUrl = 'http:' + comicUrl
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# a list of all the Thread objects
downloadThreads = []
# loops 14 times, creates 14 threads
for i in range(0, 1400, 100):
     downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
     downloadThreads.append(downloadThread)
     downloadThread.start()



for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
