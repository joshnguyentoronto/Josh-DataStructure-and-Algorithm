"""
Compare 2 consecutive element at a time and swap them if the first is bigger
continue compare until when the biggest element reach the end of array
then repeat the process
(exclude the last sorted part to save time)

Pros & Cons:
    Time: O(n) average and worst is O(n^2)
    Space: O(1)

"""

array = [2,6,5,3,4,7,1,0,9]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def bubble_sort(arr):
    i = len(arr)
    while i > 1:
        for f in range(0, i-1):
            if arr[f] > arr[f+1]:
                swap(arr, f, f+1)
            f += 1
        i -= 1
    return arr

# print(array)
# print(bubble_sort(array))

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('Bubble sort')
print(bubble_sort(big_array))