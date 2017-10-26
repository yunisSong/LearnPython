import os
import shelve
import pprint

print(os.getcwd())
shelfFile = shelve.open('ty.txt')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats

print(list(shelfFile.keys()))
print(list(shelfFile.values()))

shelfFile.close()
