"""
Just like suffix tree but build in array in order to save space
with indexes of array is the 'same' with the position of suffix in original string

Suffix array can be build in O(n*log^2(n)) (where n is length of string)
it can be O(n*log(n)) if it combine with LCP table (Longest Common Prefix of neighboring suffices table)
and also can be O(n) by using algorithm by Karkkainen and Sanders

Pros:
    Save space/memory than suffix tree

"""


