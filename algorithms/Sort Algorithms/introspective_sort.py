"""
Introsort (introspective sort) is a comparison based sort that consists of three sorting phases:
    Quick sort
    Heap sort
    Insertion sort
    (or Merge sort. not usually use cause we already use Quick sort that outperform merge sort)


Introsort combine all the Pros of 3 sorting algorithm to its usage.
It behave base on the data set:
    - If the # of elements in the input get fewer, it perform Insertion sort (typically 16, recommeded by research)
    - Quick sort is used to 'split' the array by finding the pivot. Optimize Quick sort by:
        Choosing the right pivot with 'median-of-3' or 'randomize' or 'middle' concept
        in the 'recursion depth', when the 'recursion depth' get higher, it use Heapsort (cause it has upper bound O(n*Log(n)))

Recursion Depth: typically chosen as 2 x Log2(n) with n is length of array
    This to make sure the worst case is O(n*Log(n)) 

Pros & Cons:
    Time: O(n*Log(n)) average and worse case
    Space: 
    Only use with Array*
"""



import math
from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
small_array = [2,6,5,3,4,7,1,1, 2, 2, 4, 6, 6, 7, 7, 7, 7, 8, 8, 12, 13, 13, 14, 15, 16, 16, 18, 19, 20, 21, 21, 24, 25, 26, 28, 33, 33, 34, 35, 36, 38, 40, 41, 42, 44, 46, 49, 49, 51, 52, 52, 53, 54, 55, 56, 56,6,5,3,4,7,1,1, 2, 2, 4, 6, 6, 7, 7, 7, 7, 8, 8, 12, 56, 57, 60, 62, 64, 64, 64, 65, 66, 66,0,9]




"""
Insertion Sort
"""
def insertion_sort(arr):
    print('insertion')
    cur = 0
    while cur < len(arr):
        temp = cur
        while arr[temp] < arr[temp-1] and temp > 0:
            arr[temp], arr[temp-1] = arr[temp-1], arr[temp]
            temp -= 1
        cur += 1
    return arr



"""
Heap Sort

Need to take a look again, it doesn't call on heap sort
"""
def left(i):
    return (2 * i) + 1
def right(i):
    return (2 * i) + 2
def parent(i):
    return ( ( i - 1) // 2 )
def fix_up(arr, i):
    while parent(i) >= 0 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)
def fix_down(arr, size, i):
    while left(i) < size:
        j = left(i)
        if j < size-1 and arr[j] < arr[j+1] :
            j += 1
        if arr[i] >= arr[j]:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i = j
def heapify(arr):
    print('Heapify')
    n = len(arr)
    last = n - 1
    par = parent(last)
    while par >= 0:
        fix_down(arr, n, par)
        par -= 1
    return arr
def heap_sort(arr):
    print('Heap')
    # Heapify to maxheap
    arr = heapify(arr)
    # Sorting
    n = len(arr)
    last = n - 1
    while last >= 1:
        arr[0], arr[last] = arr[last], arr[0]
        n -= 1
        last -= 1
        fix_down(arr, n , 0)
    return arr





"""
Quick Sort
"""
def med_of_three(arr, first, mid, last):
    a = arr[first]
    b = arr[mid]
    c = arr[last]
    if a <= b <= c or c <= b <= a:
        return mid
    if a <= c <= b or b <= c <= a:
        return last
    return first
# def quick_sort(arr, first, last):
#     if last <= first:
#         return
#     mid = (first + last) // 2 
#     median = med_of_three(arr, first, mid, last)
#     pivot = arr[median]
#     arr[median], arr[first] = arr[first], arr[median]
#     pos = last
#     for i in range(last, first, -1):
#         if pos > first and arr[i] > pivot:
#             arr[pos], arr[i] = arr[i], arr[pos]
#             pos -= 1
#     arr[pos], arr[first] = arr[first], arr[pos]
#     quick_sort(arr, first, pos - 1)
#     quick_sort(arr, pos + 1, last)
#     return arr





"""
Intro-Sort
"""
def helper(arr, begin, end, depth_limit):
    # print('=======QuickSort=======')
    # print(depth_limit)
    size = end - begin
    # Catch if it's done
    if end - begin <= 1:
        return
    # if reach (aka run out of) depth_limit, then perform heap_sort to minimize time to O(n*Log(n))
    elif depth_limit == 0:
        return heap_sort(arr)
    # if lower than 16, perform insertion sort
    elif size <= 16:
        return insertion_sort(arr)
    # Quick sort and Recursion in this block (not entirely in the Quick_sort function)
    else:
        mid = (begin + end) // 2 
        median = med_of_three(arr, begin, mid, end)
        pivot = arr[median]
        arr[median], arr[begin] = arr[begin], arr[median]

        pos = end
        for i in range(end, begin, -1):
            if pos > begin and arr[i] > pivot:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos -= 1
        arr[pos], arr[begin] = arr[begin], arr[pos]
        helper(arr, begin, pos - 1, depth_limit - 1)
        helper(arr, pos + 1, end, depth_limit - 1)
        return arr



def introspective_sort(arr):
    n = len(arr)
    depth_limit = 2 * math.floor( math.log2(n-1) )
    helper(arr, 0, n-1, depth_limit)




introspective_sort(small_array)
print(small_array)
print('====================================')
introspective_sort(big_array)
print(big_array)



"""
For Reference
"""
# def introsort(arr):
#     # Max depth = 2 * (floor(log2(len(arr))))
#     maxdepth = (len(arr).bit_length() - 1)*2
#     introsort_helper(arr, 0, len(arr), maxdepth)

# def introsort_helper(arr, start, end, maxdepth):
#     # print("Intro - Quick sort")
#     print(maxdepth)
#     if end - start <= 1:
#         return
#     elif maxdepth == 0:
#         heapsort(arr, start, end)
#     else:
#         p = partition(arr, start, end)
#         introsort_helper(arr, start, p+1, maxdepth - 1)
#         introsort_helper(arr, p+1, end, maxdepth - 1)

# def partition(arr, start, end):
#     pivot = arr[start]
#     i = start - 1
#     j = end

#     while True:
#         i += 1
#         while arr[i] < pivot:
#             i += 1
        
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
        
#         if i >= j:
#             return j

#         swap(arr, i, j)

# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]

# def heapsort(arr, start, end):
#     print("Heapsort")
#     build_max_heap(arr, start, end)
#     for i in range(end - 1, start, -1):
#         swap(arr, start, i)
#         max_heapify(arr, index=0, start=start, end=i)

# def build_max_heap(arr, start, end):
#     def parent(i):
#         return (i-1)//2
#     length = end - start
#     index = parent(length - 1)
#     while index >= 0:
#         max_heapify(arr, index, start, end)
#         index -= 1

# def max_heapify(arr, index, start, end):
#     def left(i):
#         return 2*i + 1
#     def right(i):
#         return 2*i + 2

#     size = end - start
#     l = left(index)
#     r = right(index)
#     if (l < size and arr[start + l] > arr[start + index]):
#         largest = l
#     else:
#         largest = index
#     if (r < size and arr[start + r] > arr[start + largest]):
#         largest = r
#     if largest != index:
#         swap(arr, start+largest, start+index)
#         max_heapify(arr, largest, start, end)

# introsort(big_array)
# print(big_array)