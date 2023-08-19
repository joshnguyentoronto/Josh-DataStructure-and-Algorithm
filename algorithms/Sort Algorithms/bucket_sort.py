"""
Bucket sort is algorithm that sort an array by distribute element in (origin) to n bucket
    then sort these bucket (usually insertion sort)
    then join the bucket together one by one

The Bucket can be linkedlist or array & usually have same length with (origin)

Pros & Cons:
    Time: average O(n + k) with k is # of buckets
    Time: worst case O(n^2)
    Space: O(n + k)
    Best use for Floating-point number
"""


array = [2.62,1.64,8.12,7.44,7.03,2.7,2.63,9.81,6.83,8.01,3.21,1.31,1.06,1.28,1.99,1.67,4.46,9.4,3.3,5.87]

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
    return

def bucket_sort(arr):
    # Create (buckets) and insert (origin) element into it
    buckets = [None] * len(arr)
    for i in range(len(arr)):
        n = int((len(arr) * arr[i]) / 10)
        if buckets[n] is None:
            buckets[n] = [arr[i]]
        else:
            buckets[n].append(arr[i])
    # Sort each bucket with insertion sort
    for bucket in buckets:
        if bucket is not None:
            insertion_sort(bucket)
    # Join all bucket together 
    arr = []
    for bucket in buckets:
        if bucket:
            for j in range(len(bucket)):
                arr.append(bucket[j])
    return arr



from number_list import ArrayTest
arr = ArrayTest()
big_array = arr.array
print('Bucket_sort')
print(bucket_sort(array))