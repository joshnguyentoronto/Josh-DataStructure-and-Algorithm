"""
In order to use binary search, we first need to sort the array
Then search the middle of array and from that continue


Pros & Cons:
    Time: O(log(n))
    Space: O(1)
    Simple
    Need to sort so time complexity need to plus sorting time
"""



arr = [1,9,15,26,32,34,34,59,68,71,72,88,90,99]


# Iterative method
def binary_search_iterative(arr, start, end, value):
    while start <= end:
        mid = (start + end) // 2
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            start = mid + 1
        elif value < arr[mid]:
            end = mid - 1
    return 'cannot find ' + str(value)


# Recursive method
def binary_search_recursive(arr, start, end, value):
    if start <= end:
        mid = (start + end) // 2
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            return binary_search_recursive(arr, mid+1, end, value)
        elif value < arr[mid]:
            return binary_search_recursive(arr, start, mid-1, value)
    else:
        return 'cannot find ' + str(value)


"""
it's shown that 'recursive' method is much faster
"""
print(binary_search_iterative(arr, 0, len(arr)-1, 71))
print(binary_search_iterative(arr, 0, len(arr)-1, 15))
print(binary_search_iterative(arr, 0, len(arr)-1, 34))
print(binary_search_iterative(arr, 0, len(arr)-1, 86))

print(binary_search_recursive(arr, 0, len(arr)-1, 15))
print(binary_search_recursive(arr, 0, len(arr)-1, 71))
print(binary_search_recursive(arr, 0, len(arr)-1, 34))
print(binary_search_recursive(arr, 0, len(arr)-1, 86))

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.sorted_array
array = [1,9,15,26,32,34,34,59,68,71,72,88,90,99]
print('binary_search')
# print(binary_search(array, 8))
print(binary_search_iterative(big_array, 0, len(big_array) -1, 5997))
print(binary_search_iterative(big_array, 0, len(big_array) -1, 3333))