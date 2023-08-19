"""
Jump search is a type of 'interval search' algorithm
    work on 'sorted list'
    each iteration, we skip a fixed # of  element (called a block)


Pros & Cons:
    Time: best - average - worst: O(1) - O(sqrt(n)) - O(sqrt(n))
    Space: 
    Search on Sorted Array
"""
import math


def jump_search(arr, value):
    if value == arr[0]:
        return 0
    temp = math.floor(math.sqrt(len(arr)))
    while value > arr[temp]:
        temp *= 2
    for i in range(math.floor(temp/2), temp):
        if value == arr[i]:
            return i
    return str(value) + ': not found'


from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.sorted_array
array = [0,1,2,3,4,5,6,7,9]
print('jump_search')
# print(jump_search(array))
print(jump_search(array, 8))
print(jump_search(big_array, 30))
print(jump_search(big_array, 366))