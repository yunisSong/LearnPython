
def binary_search(array,item):
    low = 0
    high = len(array) - 1
    print("large index is %d"%high)

    while low <= high:
        mid = int((low + high)/2)
        guess = array[mid]
        print("Mid is %d"%mid)
        print("guess is %d"%guess)
        if  guess == item:
            return mid
        elif guess < item:
            low = mid + 1
            print("+++++++low is %d"%low)
        elif guess > item:
            high = mid - 1
            print("-------high is %d"%high)
        else:
            return None
myList = [1,3,7,9,12,23,45,67,89,123,244,345,456,1234]
print(binary_search(myList,23))
