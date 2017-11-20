
def sum(arr):
    count = len(arr)
    if count == 0:
        return 0
    else:
        temp =  arr.pop(0)
        return (int(temp) + int(sum(arr)))
arr = [5, 3, 6, 2, 10]
print(sum(arr))
