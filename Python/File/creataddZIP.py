# -*- coding: UTF-8 -*-
import os,zipfile
os.chdir('/Users/Yunis/Desktop/学习/Python/zipfile')
# 创建压缩文件
newZip = zipfile.ZipFile('new.zip','w')
# 把 t.txt 文件 写入 压缩文件内 compress_type ：压缩方式
newZip.write('t.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
