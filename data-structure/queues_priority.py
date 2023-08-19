"""
Implemented in few ways:
    Array(list) of many tuple (1, "one item") with the first one is the priority
    Heap (Binary Heap)  **Most common implementation**

It can be either Max-oriented or Min-oriented
Main operations are:
    Insert
    Delete Max (or Min)
Priority Queue was used in many advance graph algorithm like:
    Dijstra's Algorithm
    A* Search Algorithm
"""




"""
Array implementation has its drawback
1st implementation:
    We Insert an item into the array {O(1)} 
    and Find the max (min) priority and return it {O(n)}
2nd implementation:
    We Insert an item into the Sorted Array {O(n)}
    and Return (and delete) the last item in the array {O(1)}
"""






"""
Heap or Binary Heap help us to insert and delete max in a more efficient way


It had the property of a Binary Tree:
    each parent node has 2 children Left & Right
Plus Structural Properties:
    each level of the Tree is completely filled (except for the last level)
    the tree is filled from the left to the right
    the structure will alway be Balanced -> so the height always = Log(n) (with n is number of nodes)
Plus Heap-order Properties:
    (Max heap): Parent key is alway larger (or equal) to its left & right children
    (or Min heap): Parent key is alway smaller (or equal) to its left & right children


We can implement the Binary Heap with either an Array or Binary Tree
Array = [30, 19, 25, 18, 15, 2,  4,  5, 16 ]
        [0]  [1] [2] [3] [4] [5] [6] [7] [8]
Binary Tree:
                    30
                    [0]
        19                       25
        [1]                      [2]
    18        15            2           4
    [3]       [4]          [5]         [6]
 5      16
[7]     [8]

Left Child of index i
    2 * i + 1
Right Child of index i
    2 * i + 2
Parent of index i
    math.ceil ( ( i - 2 ) / 2 )
    or math.floor ( ( i - 1) / 2 )

Implement Heap by Array is more effective than by Tree {O(log n)}
    They are Asymptotically same Time & Space complexity
    But Tree use more time & memory(to store data + 2 pointers)
    And in Tree, Node allocation and de-allocation takes longer than insert and delete in an array(list)
"""







"""
Heap implemented with Array:
"""

class MaxHeap:
    def __init__(self):
        self.arr = []
        self.size = 0
    def __repr__(self):
        ar = []
        for i in range(len(self.arr)):
            ar.append(str(self.arr[i]))
        return '[' + ', '.join(ar) + ']' + '\nHeap size of ' + str(self.size)

# Helper function:
# Find node (index)
import math
def left(i):
    return (2 * i) + 1
def right(i):
    return (2 * i) + 2
def parent(i):
    return math.ceil((i - 2) / 2)

# Swap position
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

# Perform Fix-up(insert at the end of array and sort fix-up)
# && Fix-down(remove the max at the top arr[0], replace it with the last item in the arr and sort fix-down )
def fix_up(arr, i):
    while parent(i) >= 0 and arr[parent(i)] < arr[i]:
        swap(arr, i, parent(i))
        i = parent(i)

def fix_down(arr, size, i):
    while left(i) < size:
        j = left(i)
        if arr[j] < arr[j+1] and j < size-1:
            j += 1
        if arr[i] >= arr[j]:
            break
        swap(arr, i, j)
        i = j

def insert(heap, x):
    heap.size += 1
    heap.arr.append(x)
    fix_up(heap.arr, heap.size - 1)
    return heap.arr

def delete_max(heap):
    swap(heap.arr, 0, heap.size - 1)
    heap.size -= 1
    fix_down(heap.arr, heap.size, 0)
    return heap.arr.pop()

myheap = MaxHeap()
print(myheap)
print(insert(myheap, 30))
print(insert(myheap, 25))
print(insert(myheap, 19))
print(insert(myheap, 2))
print(insert(myheap, 4))
print(insert(myheap, 5))
print(insert(myheap, 16))
print(insert(myheap, 15))
print(insert(myheap, 18))
print('===========')
print(myheap)
print(delete_max(myheap))
print(myheap)
print(delete_max(myheap))
print(myheap)
print(delete_max(myheap))
print(myheap)
print(delete_max(myheap))
print(myheap)





"""
Heapify: turn an array into max heap (or min heap)
Time: O(n)
Space: O(1)
(bad implementation may require O(n) space)
"""
array = [2,6,5,3,4,7,1,0,9]
def max_heapify(arr):
    n = len(arr)
    last = n - 1
    par = parent(last)
    while par >= 0:
        fix_down(arr, n, par)
        par -= 1
    return arr

print('------Max-Heapify------')
print(max_heapify(array))



"""
Heap Sort
check heap_sort.py
"""
def heap_sort(arr):
    # Heapify to maxheap
    arr = max_heapify(arr)
    # Sorting
    n = len(arr)
    last = n - 1
    while last >= 1:
        swap(arr, 0, last)
        n -= 1
        last -= 1
        fix_down(arr, n , 0)
    return arr

print('------Heap_Sort------')
print(array)
print(heap_sort(array))



"""
Heap implemented with Binary Tree (to practice):
"""








