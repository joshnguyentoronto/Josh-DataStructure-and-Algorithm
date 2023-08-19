"""
Fibonacci search is similar to 'binary search' that use divide and conquer technique
    but instead divide array in 2
    it divide array into 2 'un-equal' part 

Pros & Cons:
    Time: 
    Space: 
    Need sorted array
    Better than 
"""

def fibonacci_search(arr, value):
    fib0 = 0
    fib1 = 1
    fib = fib0 + fib1
    while fib < len(arr):
        fib0 = fib1
        fib1 = fib
        fib = fib0 + fib1
    offset = -1
    while fib > 1:
        # Check if fib0 is value location
        i = min(offset + fib0, len(arr)-1)
        if arr[i] < value:
            fib = fib1
            fib1 = fib0
            fib0 = fib - fib1
            offset = i
        elif arr[i] > value:
            fib = fib0
            fib1 = fib1 - fib0
            fib0 = fib - fib1
        else:
            return i

    if fib1 and arr[len(arr)-1] == value:
        return len(arr) - 1
    return "not found"


from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.sorted_array
array = array = [0,1,2,3,4,5,6,7,9]
print('fibonacci_search')
print(fibonacci_search(array, 3))
print(fibonacci_search(array, 8))
print(fibonacci_search(big_array, 4355))
print(fibonacci_search(big_array, 30))