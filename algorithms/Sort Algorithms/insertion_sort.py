"""
Sort from the left to right
    Compare each element to the left of it
    if it's smaller to the left, move it to the left until it is in position 
    (move many steps till the new left is smaller and the right is bigger)


Pros & Cons:
    Time: O(n) average and worst is O(n^2)
    Space: O(1)
    Good performance with small List but not with large data set
"""


array = [2,1,6,9,3,5,3,4,7,1,0,9]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def insertion_sort(arr):
    cur = 0
    while cur < len(arr):
        temp = cur
        while arr[temp] < arr[temp-1] and temp > 0:
            swap(arr, temp, temp-1)
            temp -= 1
        cur += 1
    return arr

# print(array)
# print(insertion_sort(array))

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('insertion_sort')
print(insertion_sort(big_array))