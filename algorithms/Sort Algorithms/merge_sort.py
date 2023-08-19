"""
Divide and conquer method

Merge sort goes well with Array or Linkedlist

Given an array
    divide the array by half and sort each of them
    can use iterative method or recursion method

Pros and Cons:
    Stable
    Time: O( n*Log(n) )
    Space: O(n)

"""
import math
array = [2,6,5,3,4,7,1,0,9]

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        ileft = iright = i = 0
        while ileft < len(left) and iright < len(right):
            if left[ileft] < right[iright]:
                arr[i] = left[ileft]
                ileft += 1
            else:
                arr[i] = right[iright]
                iright += 1
            i += 1
        while ileft < len(left):
            arr[i] = left[ileft]
            ileft += 1
            i += 1
        while iright < len(right):
            arr[i] = right[iright]
            iright += 1
            i += 1
    return arr


print(merge_sort(array))

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('merge sort')
print(merge_sort(big_array))