import time, subprocess
print('Start')
timeLeft = 5
while timeLeft > 0:
    print('Left')
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

print('Play')
subprocess.Popen(['open', '/Users/Yunis/Documents/Github/LearnPython/Python/Time/01.mp3'])
