"""
Comb sort is like bubble sort but trying to improve by using gap of size more than 1

The 'Gap' k start at large value, then reduce to (k / 1.3)

Pros & Cons:
    Time: 
    Space: 
"""
import math

array = [2,6,5,3,4,7,1,0,9]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def Comb_sort(arr):
    gap = i = len(arr)
    
    while gap > 0:
        for f in range(0, i - gap):
            if arr[f] > arr[f+gap]:
                swap(arr, f, f+gap)
        gap = math.floor(gap / 1.3)
    return arr



from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('Comb_sort')
print(Comb_sort(big_array))