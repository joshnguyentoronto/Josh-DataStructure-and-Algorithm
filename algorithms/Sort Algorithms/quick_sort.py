"""
Devide and Conquer method

Quick_sort goes well with Array but not Linkedlist
Quick_sort is used more than Merge_sort cause it save more space and can be optimize with right pivot

Given an array
    chose the first item as pivot 
    Median-of-Three (or compare the first, mid, and last of the array, pick the mid in one of these to maximize the efficiency)
    then from last of array (pos), compare it with pivot
    if bigger than pivot, swap it to the right
    if smaller than pivot, swap it to the left
    then swap the pivot with the middle index (pos)
    then recursive with each sub array

Pros & Cons:
    Easy to understand
    Time:  O( n*Log(n) ) ==> O(n^2)
    Space {O(1)} 
    Not stable (order of element in array is not stable)
"""
import math

array = [2,6,5,2,6,5,3,4,0,9]


def med_of_three(arr, first, mid, last):
    a = arr[first]
    b = arr[mid]
    c = arr[last]
    if a <= b <= c or c <= b <= a:
        return mid
    if a <= c <= b or b <= c <= a:
        return last
    return first

def quick_sort(arr, first, last):
    if last <= first:
        return
    mid = math.floor( (first + last) / 2 )
    median = med_of_three(arr, first, mid, last)
    pivot = arr[median]
    arr[median], arr[first] = arr[first], arr[median]
    pos = last
    for i in range(last, first, -1):
        if pos > first and arr[i] > pivot:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos -= 1
    arr[pos], arr[first] = arr[first], arr[pos]
    quick_sort(arr, first, pos - 1)
    quick_sort(arr, pos + 1, last)
    return arr


# print( quick_sort(array, 0, len(array)-1) )

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('Quick sort')
print(quick_sort(big_array, 0, len(big_array)-1))