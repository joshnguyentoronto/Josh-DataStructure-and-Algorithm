"""
Anytime we add item to an array, 
    instead of creating a fix array and then when it's full, create another bigger array and copy the old one to the new array,
    time complexity when adding will be O(n)
    when it's full, we create a new array that dobble the size of the old array
    time complexity when adding will be O(1) amortized
    1 + 2 + 4 + 8 + ... + n/8 + n/4 + n/2   =>   (n - 1) / n   =>   O(1)
"""