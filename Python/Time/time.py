import time

def calcProd():
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
time.sleep(5)

now = time.time()
print(now) #1509609194.070355
print(round(now,2)) #1509609194.07
print(round(now,4)) #1509609194.0704
