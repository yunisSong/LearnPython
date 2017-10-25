# -*- coding: UTF-8 -*-
# mcb.pyw - Saves and loads pieces of text to the clipboard.
#  Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#         py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#         py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys
# .pyw 扩展名意味着 Python 运行该程序时，不会显示终端窗口

# 进入工作目录
os.chdir('/Users/Yunis/Desktop/学习/Python/mcb')
# 打印当前工作目录
print("当前工作目录为 %s"%(os.getcwd()))

# shelve是一额简单的数据存储方案，他只有一个函数就是open()，这个函数接收一个参数就是文件名，然后返回一个shelf对象，你可以用他来存储东西，就可以简单的把他当作一个字典，当你存储完毕的时候，就调用close函数来关闭

# 建立一个存储容器
mcbShelf = shelve.open('mcb')

# 判断参数有几个，
if len(sys.argv) == 3:
    # 判断第2个参数是否为save
    if sys.argv[1].lower() == 'save' :
        # 把粘贴板的值保存在 mcbShelf
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif  sys.argv[1].lower() == 'del' :
        # 删除关键字对应的值
        mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        # 把容器中保存的key 填充到粘贴板
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        # 根据传的参数，把容器中对应key的值取出来放置在粘贴板中
        pyperclip.copy(mcbShelf[sys.argv[1]])
# 关闭
mcbShelf.close()
