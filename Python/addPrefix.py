# -*- coding: UTF-8 -*-
import shutil,os,re

def addPrefixInpath(path):
    # 获取文件路径下的文件集合
    # print(path)
    # 创建正则表达式
    # 获取文件路径下的文件集合
    for amerFilename in os.listdir(path):
        # 组成新的文件名
        euroFilename = 'YunisAdd' + amerFilename
        absWorkingDir = os.path.abspath(path)
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)
        print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
        shutil.move(amerFilename, euroFilename) # uncomment after testing

addPrefixInpath('/Users/Yunis/Desktop/学习/Python/date')
