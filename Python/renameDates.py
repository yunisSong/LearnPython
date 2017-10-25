# -*- coding: UTF-8 -*-
import shutil,os,re

def renameDatesInpath(path):
    # 获取文件路径下的文件集合
    # print(path)
    # 创建正则表达式
    datePattern = re.compile(r'^(.*?)((0|1)\d)-((0|1|2|3)\d)-((19|20)\d\d)(.*?)$')

    # 获取文件路径下的文件集合
    for amerFilename in os.listdir(path):
        # 正则表达式对象匹配结果
        # Regex 对象的 search()方法查找传入的字符串，寻找该正则表达式的所有匹配。如 果字符串中没有找到该正则表达式模式，search()方法将返回 None。如果找到了该模式， search()方法将返回一个 Match 对象。Match 对象有一个 group()方法，它返回被查找字 符串中实际匹配的文本
        mo = datePattern.search(amerFilename)
        # 如果这个文件没有匹配，开始匹配下个文件
        if mo == None :
            continue
        # re.compile(r'^(.*?)((0|1)\d)-((0|1|2|3)\d)-((19|20)\d\d)(.*?)$')
        # group index
        # datePattern = re.compile(r'^(1)((2)3)-((4)5)-((6)7)(8)$')

        # 获取 Match 对象 对应的字符串
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
        # 组成新的文件名
        euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart


        absWorkingDir = os.path.abspath(path)
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)
        print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
        shutil.move(amerFilename, euroFilename) # uncomment after testing

renameDatesInpath('/Users/Yunis/Desktop/学习/Python/date')
