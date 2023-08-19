"""
Ternary search is similar to binary search
    but instead of divide the array by half
    we divide it into 3 part
    and chose 1 of 3 part to continue to search, ignore the other 2

Pick 2 middle point:
    Array[start, end]
    mid1 = start + (end - start)/3
    mid2 = end - (end - start)/3
    (AKA start + 1/3 length AND end - 1/3 length)

Pros & Cons:
    Time: best - average - worst: O(1) - O(Log3(n)) - O(Log3(n))
    Space: O(1)
    Need Sorted array
    Simple
    More efficient than binary search
"""
import math


def ternary_search(arr, start, end, value):
    if start <= end:
        mid1 = math.ceil(start + (end - start)/3)
        mid2 = math.ceil(end - (end - start)/3)
        if value == arr[start]:
            return start
        elif value == arr[end]:
            return end
        if value == arr[mid1]:
            return mid1
        elif value == arr[mid2]:
            return mid2
        elif value < arr[mid1]:
            return ternary_search(arr, start, mid1 - 1, value)
        elif arr[mid1] < value and value < arr[mid2]:
            return ternary_search(arr, mid1 + 1, mid2 - 1, value)
        elif arr[mid2] < value:
            return ternary_search(arr, mid2 + 1, end, value)
    else:
        return str(value) + ": not found"

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.sorted_array
array = [2,1,6,9,3,5,3,4,7,1,0,9]
print('ternary_search')
# print(ternary_search(array))
print(ternary_search(big_array, 0, len(big_array)-1, 33))
print(ternary_search(big_array, 0, len(big_array)-1, 3463))