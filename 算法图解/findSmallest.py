
# 找出当前数组最小的数字的index
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 选择排序  O(n²)
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        # arr.pop(smallest_index) 移除指定位置的元素，并返回这个元素
        newArr.append(arr.pop(smallest_index))
    return newArr


print (selectionSort([5, 3, 6, 2, 10]))
