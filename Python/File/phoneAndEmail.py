# -*- coding: UTF-8 -*-
import string
import random,sys,os
import re

someRegexValue = re.compile(r'(^\d{1,3})(,\d{3})*$')

resoce = ['1,333,444',',333,444','333,444','33,444','3,444',',444','444','44','4','1,']
for i in resoce:
    mo = someRegexValue.search(i)
    if mo is None:
        print(i + "  不符合");
    else:
        print(str(mo.group()) + '  符合')
password = input()


print(password)

def isStrongPs(password):
    #判断是否包含大写和小写字母
    r1 = re.compile(r'')
 re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\
re.IGNORECASE)
    #判断是否包含数字
    #判断长度是否大于等于8
    return False
