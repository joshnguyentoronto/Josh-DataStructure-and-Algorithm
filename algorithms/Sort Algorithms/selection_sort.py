"""
Naive method 


Given an array
    compare each index with all other
    pick the smallest index 
    and then swap it to the last one in an sorted array part

Pros & Cons:
    Easy to understand
    cost time {O(n^2)} 
    space {O(1)}
"""


array = [2,8,5,3,9,4,1]


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        swap(arr, min, i)
        print(arr)
    return arr


print(selection_sort(array))