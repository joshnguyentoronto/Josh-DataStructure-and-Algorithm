"""
Shell sort is a 'variation' of 'insertion sort'
While insertion sort compare an element to the one left of it
Shell sort compare an element to the one N block on the left of it
Then gradually reduce the N block to 1 and then 0 (to stop)
(it may also move many steps (like insertion sort) till the new left is smaller and the right is bigger)


Pros & Cons:
    Time: average+best: O( n * Log(n) )
    Time: worst: O( n * (Log(n))^2 )
    Space: O(1)
"""


array = [2,6,5,3,4,7,1,0,9]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def insertion_sort(arr):
    cur = 0
    while cur < len(arr):
        temp = cur
        while arr[temp] < arr[temp-1] and temp > 0:
            swap(arr, temp, temp-1)
            temp -= 1
        cur += 1
    return arr

def shell_sort(arr, leng):
    gap = leng // 2
    while gap > 0:
        # set-up index
        index = gap
        # index must be withing array
        while index < leng:
            # this to maintain gap value within the array
            i = index - gap
            while i >= 0:
                # Check the right side
                if arr[i+gap] > arr[i]:
                    break
                else:
                    swap(arr, i+gap, i)
                # Check left side also
                i = i - gap
            index += 1
        gap = gap // 2
    return arr



from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('shell_sort')
print(shell_sort(big_array,len(big_array)))