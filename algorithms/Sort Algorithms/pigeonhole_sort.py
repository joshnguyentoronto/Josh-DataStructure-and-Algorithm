"""
Pigeonhole sort is suitable for Array of ele,
    where # of ele and # of possible key value are approximately the same

Pigeonhole sort is similar to Counting sort. But it move the items 'twice'
    1 to the bucket array
    2 to the final destination

Implementation:
    Find max and min of (origin)
    Create (pigeonhole) size of 'max - min + 1'
    Insert value in (origin) to (pigeonhole) with 'index' = arr[i] - min & 'value' = (origin) 'value'
    Loop through (pigeonhole) and insert 1 by 1 to the (origin)

Pros & Cons:
    Time: O(n + k)
    Space: O(n + k)
        with n is # of item of array
        with k is the range of number that is in the array
        ex: max of array if 9 --> range is 9
    Stable
    Only Best if the range of number is small within the array
"""


array = [2,1,6,9,3,5,3,4,7,1,0,9]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def pigeonhole_sort(arr):
    maxi = max(arr)
    mini = min(arr)
    temp = [None] * (maxi - mini + 1)
    for i in arr:
        if temp[i-mini] is None:
            temp[i-mini] = [i]
        else:
            temp[i-mini].append(i)
    arr = []
    for array in temp:
        if array is not None:
            for i in range(len(array)):
                arr.append(array[i])
    return arr



from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('pigeonhole_sort')
# print(array)
# print(pigeonhole_sort(array))
print('pigeonhole_sort')
print(pigeonhole_sort(big_array))