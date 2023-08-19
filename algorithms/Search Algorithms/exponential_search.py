"""
Exponential search is similar to binary search but 'in reverse'
    start with a variable pos=0 compare the target value with arr[pos]
    if pos < value: then double the pos: pos * 2
    if pos > value: then perform 

Pros & Cons:
    Time: O(1) - O(log(n))
    Space: 

"""
import math

def binary_search(arr, start, end, value):
    while start <= end:
        mid = math.floor((start + end) // 2)
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            start = mid + 1
        elif value < arr[mid]:
            end = mid - 1
    return 'cannot find ' + str(value)

def exponential_search(arr, value):
    pos = 0
    while pos < len(arr) and value >= arr[pos]:
        if value == arr[pos]:
            return pos
        if pos == 0:
            pos += 1
        pos *= 2
    if pos > len(arr):
        return binary_search(arr, pos/2, len(arr)-1, value)
    else:
        return binary_search(arr, pos/2, pos, value)


from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.sorted_array
array = [0,1,2,3,4,5,6,7,9]
print('exponential_search')
print(exponential_search(array, 3))
print(exponential_search(array, 8))
print(exponential_search(big_array, 4355))
print(exponential_search(big_array, 30))