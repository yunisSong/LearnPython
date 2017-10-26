# -*- coding: UTF-8 -*-
import os,zipfile

os.chdir('/Users/Yunis/Desktop/学习/Python/zipfile')
exampleZip = zipfile.ZipFile('t.txt.zip')
# 获取压缩文件集合
print(exampleZip.namelist())
# 获取指定文件信息
spamInfo = exampleZip.getinfo('t.txt')
# 文件真实大小
print(spamInfo.file_size)
# 文件压缩后的大小
print(spamInfo.compress_size)
exampleZip.close()
