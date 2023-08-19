"""
(origin) (temp) (result) array
    First create an array (temp) size K (unknown) and count each recursive number within (origin)
        value of each <element> in (origin) is <index> of (temp)
        and value of <index> of (temp) is the count of each number
    Then add each element in (temp) array to the number before itself
    Then Shift the value of this (temp) array to 1 index (the first element will be 0, and we delete the last element)
        The (temp) now show the position of each element in (origin) that should be in the (result)
    Create a new array to shift the original array into it following the position in (temp)
        This is [stable] cause we iterate through original array,
            and the first recursive number is added 'first'
            the second recursive number is added 'second'
            and so on

Pros & Cons:
    Time: O(n + k)
    Space: O(n + k)
    Stable
    with n is # of item of array
    with k is the range of number that is in the array
        ex: max of array if 9 --> range is 9
    Only Best if the range of number is small within the array
"""


array = [2,3,5,3,4,3,1,0,2]

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def counting_sort(arr):

    # First create an array (temp) size K (unknown) and count each recursive number within array
    temp = []
    for i in range(len(arr)):
        if arr[i] + 1 > len(temp):
            n = 0
            len_temp = len(temp)
            while n <= (arr[i] - len_temp):
                temp.append(0)
                n += 1
        temp[arr[i]] += 1

    # Then add each element in (temp) array to the number before itself
    for i in range(1, len(temp)):
        temp[i] = temp[i] + temp[i-1]

    # Then Shift the value of this (temp) array to 1 index
    temp.pop()
    temp.insert(0, 0)

    # Create a new array to shift the original array into it following the position in (temp)
    result = [0] * len(arr)
    for i in arr:
        result[temp[i]] = i
        temp[i] += 1
    # return result
    return


# print(array)
# print(counting_sort(array))

from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('Counting sort')
print(counting_sort(big_array))