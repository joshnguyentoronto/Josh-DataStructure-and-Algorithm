"""
Interpolation search is mainly used in a 'uniformly distributed' and 'sorted list'

a 'uniformly distributed' list is list that the difference between each element is equal

In 'uniformly distributed, sorted list', we have a 'formula' to calculate the 'probable position' of the target:
    array[start, end]
    array[probable position] = target value
    probable position = start + (target value - array[start]) * (end - start) / (array[high] - array[low])

Implementation:
    Similar to binary search
    but instead choosing the middle element, we choose the probable position and value to compare
    cause the list is uniformly distributed


Pros & Cons:
    Time: best - average - worst: O(1) - O(Log( Log(n) )) - O(n)
    Space: 

"""
import math


def interpolation_search(arr, start, end, value):
    while start < end:
        pos = math.floor(start + (value - arr[start]) * (end - start) / (arr[end] - arr[start]))
        if value == arr[pos]:
            return pos
        elif value < arr[pos]:
            return interpolation_search(arr, start, pos-1, value)
        elif value > arr[pos]:
            return interpolation_search(arr, pos+1, end, value)
    return str(value) + ': not found'


from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.sorted_array
array = [0,1,2,3,4,5,6,7,9]
print('interpolation_search')
# print(interpolation_search(array))
print(interpolation_search(array, 0, len(array)-1, 4))
print(interpolation_search(array, 0, len(array)-1, 8))
print(interpolation_search(big_array, 0, len(big_array)-1, 30))
print(interpolation_search(big_array, 0, len(big_array)-1, 3236))