# -*- coding: UTF-8 -*-
import os,zipfile
os.chdir('/Users/Yunis/Desktop/学习/Python/zipfile')
exampleZip = zipfile.ZipFile('t.txt.zip')
# 解压缩所用文件和文件夹 'Yunis' 为路径参数，表示解压缩到这个路径，参数为空表示解压缩到当前路径
# exampleZip.extractall('Yunis')
# 解压缩 单个't.txt' 文件到 'SSY' 路径下，路径为空解压到当前路径
exampleZip.extract('t.txt','SSY')
exampleZip.close()
