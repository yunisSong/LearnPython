# -*- coding: UTF-8 -*-
import os
import re
import sys
import shutil
sourceArray = [];

def findFileInpath(path):
    # 获取文件路径下的文件集合
    # print(path)
    for filename in os.listdir(path):
        if os.path.isdir(path+'/'+filename):
            # print(path+'/'+filename)
            findFileInpath(path+'/'+filename)
        else:
            # 匹配查找图片
            datePattern = re.compile(r'(\.pdf|\.png|\.jpg)$')
            mo = datePattern.search(filename)
            # 如果这个文件没有匹配，开始匹配下个文件
            if mo == None :
                continue
            # 记录文件路径
            sourceArray.append(path + '/' +filename)
            print(path + '/' +filename)
# findFileInpath('/Users/Yunis/Documents/临时放置/ZDDB')
findFileInpath('/Users/Yunis/Desktop')

# 移除文件
# os.remove(sourceArray[0])

for filename in sourceArray:
    print(filename)
    # shutil.copy(filename, '/Users/Yunis/Desktop/testCopy')
