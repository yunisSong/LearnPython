import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print('Started.')
# 开始时间
startTime = time.time()
# 结束时间
lastTime = startTime
lapNum = 1

try:
    while True:
        # 开始输入  当敲击回车键时  输入结束
        input()
        # 计算本次输入最后的时间
        lapTime = round(time.time() - lastTime, 2)
        # 计算总时间
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        # 从新设置下次计时的时间
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
