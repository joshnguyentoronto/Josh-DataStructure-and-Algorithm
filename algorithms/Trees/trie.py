"""
Trie is a way of storing multiple strings,
    that improve search speed
    reduce redundancy by represent those strings as a set of prefixes

Ex: if we want to store "josh", "john"
    we create a node that store 'j'
    then we create a node that store 'o'
    then we create 2 children node that store 's' -> 'h' and 'h' -> 'n'

Pros:
    Easy to do exact matches
    Find string that start with a set of characters
Cons:
    Can waste storage (like Ex above, both 2 word has 'jo' but we store them differently 'j' and 'o' )
    Difficult to search 'substring' other than beginning of the word (e.g., find all word contain 'os')

Insert: O(n) O(n*m)
Search: O(n) O(1)

"""




