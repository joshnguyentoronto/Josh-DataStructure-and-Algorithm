"""
Implementation:
    create variable:
        cycleStart = 0
        current ele value 
        position of current ele (find by loop and increment when meet the equal or smaller ele)
    Loop from 0 to n-2 (each loop create a cycle)
        n-2: because when we reach the 2nd last, we can still loop
        but if we loop to n-1, when we reach the last ele, there'll be error and cannot loop
        even though the array is sorted by now
        Loop and count # of ele smaller or equal than value of this ele
        if pos == current index (aka: no smaller ele after it)
            Then skip
        if current ele value == pos's value (aka: duplicate ele)
            Then increase the pos by 1 and check again (while loop)
            So in the (sorted), this make the pos and pos+1 both at the correct pos
        Finally if pos != outerIndex (current Index) (aka: safe to swap)
            Then we can finally swap the current ele with the pos's ele
        Loop: continue this cycle (with new current ele that just swaped) by: while the pos !== outerIndex and Copy all the 'if' above
            So that we not only check if the pos !== with the start, 
            we also check if the current ele !== ele at pos index


Cycle sort create some set of 'Cycle Decomposition'
Ex: [10, 7, 1, 3, 5]
    First Cycle:
        take 10 and place in its pos (last index cause it largest)
        then take 5 and place in its pos (2nd index)
        then take 1 and place in its pos (0th index)
            because 0th index was #10's index, we end this cycle
    Second Cycle:
        take 7 and place in its pos (3rd index)
        take 3 and place in its pos (1st index)
            because 1st index was #7's index, we end this cycle
    Loop to other cycle to check --> Done
Cycle Decomposition:
    (10, 5, 1)
    (7, 3)


Pros & Cons:
    Time: O(n^2) 'even in the best case'
    Space: O(1)   
    'in-place' and also no need extra variables or buffers
    Unstable
    only best to use in 'small' array that has 'small' range of value
    theoretically optimal in term of the total # of write (modify) in the (origin)
"""


array = [2,1,6,9,3,5,3,4,7,1,0,9]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def cycle_sort(arr):
    # main loop to create each cycle
    for origin_index in range(0, len(arr) - 2):
        print("Origin_Index " + str(origin_index))
        current = arr[origin_index]
        position = origin_index
        
        # Loop to count the # that equal or smaller to 'current' and increase the 'position' -> this is new position
        for i in range(origin_index + 1, (len(arr))):
            if arr[i] < current:
                position += 1
        # check if the cycle end, if yes, end this cycle and continue with next cycle
        if position == origin_index:
            continue
        # increase pos by 1 if there is duplicate value
        if arr[position] == current:
            position += 1
        # Swap the origin element to its correct position
        if position != origin_index:
            current = arr[position]
            swap(arr, position, origin_index)
        # Continue this cycle with another same loop
        while position != origin_index:
            position = origin_index
            for i in range(origin_index + 1, (len(arr))):
                if arr[i] < current:
                    position += 1
            # Because of the While loop, this is no longer needed
            if position == origin_index:
                continue
            if arr[position] == current:
                position += 1
            # Note this 'if' is different cause the value of the loop
            if current != arr[position]:
                current = arr[position]
                swap(arr, position, origin_index)
    return arr




print('cycle_sort')
array = [10, 7, 1, 3, 5]
array = [2,1,6,9,3,5,3,4,7,1,0,9]
print(array)
print(cycle_sort(array))
