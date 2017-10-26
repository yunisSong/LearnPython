# -*- coding: UTF-8 -*-
import requests,os,sys

currentFilePath = sys.path[0]
webFilePath = os.path.join(currentFilePath, "file")
os.chdir(webFilePath)
print(os.getcwd())
res = requests.get("http://static.open-open.com/lib/uploadImg/20160623/20160623173015_416.png")
playFile = open('python.jpg', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
