"""
Check:
    queue_priority.py
    heap.py

Heap can use Array or Linkedlist (but linkedlist cost more space and take more time to traverse through the tree)

Let's use ARRAY to implement Heap

2 Ways to implement heap_sort:
    Create another array as our heap (min-heap)
        insert each element into the array and keep the structure property of it
        then extract the first element (the min) to the original array
        Pros and Cons:
            Time: O( n*Log(n) )
            Space: O(n)
    Heapiry the Original array to min heap {O(n)}
        extract first element (min) to the new array
        along with keeping the structure property of the min heap
        Pros and Cons:
            Time: O( n*Log(n) )
            Space: O(n)
    BEST: Heapify the Original array to max heap {O(n)}
        then swap the first element (max) to the last element
        decrease the size of array by 1 and call fix_down on the first (last) element that just switch to keep the structure property of the heap
        then continue till n > 1 (only 1 element left mean the rest is sorted from min to max)
        Pros and Cons:
            Time: O( n*Log(n) )
            Space: O(1)

Pros & Cons:
    Not stable (order of element in array is not stable)
    Best for Array
"""






"""
Get from queues_priority.py
Max Heap
"""
import math
def left(i):
    return (2 * i) + 1
def right(i):
    return (2 * i) + 2
def parent(i):
    return math.floor ( ( i - 1) / 2 )

# Swap position
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

# Perform Fix-up(insert at the end of array and sort fix-up)
# && Fix-down(remove the max at the top arr[0], replace it with the last item in the arr and sort fix-down )
def fix_up(arr, i):
    while parent(i) >= 0 and arr[parent(i)] < arr[i]:
        # swap(arr, i, parent(i))
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)

def fix_down(arr, size, i):
    while left(i) < size:
        j = left(i)
        if j < size-1 and arr[j] < arr[j+1] :
            j += 1
        if arr[i] >= arr[j]:
            break
        swap(arr, i, j)
        i = j

def heapify(arr):
    n = len(arr)
    last = n - 1
    par = parent(last)
    while par >= 0:
        fix_down(arr, n, par)
        par -= 1
    return arr



"""
Heap Sort
"""
def heap_sort(arr):
    # Heapify to maxheap
    arr = heapify(arr)
    # Sorting
    n = len(arr)
    last = n - 1
    while last >= 1:
        swap(arr, 0, last)
        n -= 1
        last -= 1
        fix_down(arr, n , 0)
    return arr


# array = [2,6,5,3,4,7,1,0,9]
# print(array)
# print(heap_sort(array))

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('Heapsort')
print(heap_sort(big_array))
