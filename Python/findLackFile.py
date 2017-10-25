import shutil, re, os
filedir = ''
a = os.listdir(filedir)
alist = ' '.join(a)
span = re.findall('spam(\d+).txt', alist)
span.sort()
j = 0
lenlist = []
for i in range(1,len(span)+1):
    newi = str(i)
    newistr = newi.zfill(len(span[0]))
    lenlist.append(newistr)
    if span[i-1] != lenlist[j]:
        shutil.move(filedir + '\\spam' + span[i-1] + '.txt', filedir + '\\spam' + lenlist[j] + '.txt'  )
    j += 1
print('恭喜你，所有的文件已经按顺序spam' + str(lenlist) + '.txt命名')
