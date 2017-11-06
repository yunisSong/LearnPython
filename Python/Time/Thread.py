import threading, time

print('Start of program.')

def takeANap():
    time.sleep(2)
    print('Wake up!')

def threadArgs(arg,arg1):
    time.sleep(3)
    print(str(arg) + '  ' + str(arg1))

threadObj = threading.Thread(target=takeANap)
threadObj.start()

threadArgs = threading.Thread(target=threadArgs,args=['Yunis','三十一'])
threadArgs.start()

print('End of program.')
