
def quickSort(array):
    # 判断数组是否满足基线条件，如果满足基线条件直接返回
    # 如果不满足基线条件，继续减小问题规模
    if len(array) > 1:
        mid = array[0]
        largeArray = []
        smallArray = []
        print("---------------mid = " + str(mid))
        for index in range(1,len(array)):
            value = array[index]
            if  value > mid :
                largeArray = largeArray +[value]
            else :
                smallArray = smallArray +[value]
        print("smallArrar = " + str(smallArray))
        print("largeArray = " + str(largeArray))
        return quickSort(smallArray) + [mid] + quickSort(largeArray)
    else:
        return array


def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


array = [40,15,10,15,31,27,33,32,8,48,20,4,5,45,3,26,14,6,30]
print(quickSort(array))
