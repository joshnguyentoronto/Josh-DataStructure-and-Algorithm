"""
    Search one by one
    Array doesn't need to be sorted

Pros & Cons:
    Time: O(n)
    Space: O(1)
    Simple
"""

def linear_search(arr, value):
    for i in range(len(arr)):
        if value == arr[i]:
            return i
    return "404: # not found"


from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
array = [2,1,6,9,3,5,3,4,7,1,0,9]
print('Linear_search')
# print(linear_search(array, 8))
print(linear_search(big_array, 5997))
print(linear_search(big_array, 3455))