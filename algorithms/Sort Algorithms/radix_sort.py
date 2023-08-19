"""
Radix sort can 'only' be used to sort int Number
    We sort number from the most significant diget to most significant digit
    And we use 'counting sort' as a subroutine to sort
    cause we only compare digit from 0-9

Pros & Cons:
    Time: O(n*k) 
    Space: O(n + k)
"""



def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def counting_sort(arr, exp):
    # First create an array (temp) size 10 (0-9) and count each recursive number within array
    temp = [0] * 10
    # find Modulus of number in each index to store from 0-9
    for i in range(len(arr)):
        temp_index = arr[i] // exp
        temp[temp_index % 10] += 1
    # Then add each element in (temp) array to the number before itself
    for i in range(1, 10):
        temp[i] += temp[i-1]
    # Then Shift the value of this (temp) array to 1 index
    temp.pop()
    temp.insert(0, 0)
    # Create a new array to shift the original array into it following the position in (temp)
    result = [0] * len(arr)
    for i in range(len(arr)):
        a = (arr[i] // exp) % 10
        result[temp[a]] = arr[i]
        temp[a] += 1
    for i in range(len(arr)):
        arr[i] = result[i]


def radix_sort(arr):
    # get max to know how many time to loop
    maxi = max(arr)
    # set exp as 10^i --> 1, 10, 100, 1000, ...
    exp = 1
    while maxi/exp >= 1:
        counting_sort(arr, exp)
        exp *= 10
    return arr



from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
array = [170, 45, 75, 90, 802, 24, 2, 66]



print('radix_sort')
# print(radix_sort(array))
print(radix_sort(big_array))

