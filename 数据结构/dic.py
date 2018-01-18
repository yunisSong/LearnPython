import timeit






li = [i for i in range(1000) if i%2 == 0 and i > 100]

li.insert(1000,1)
li.append(3)

print(li)