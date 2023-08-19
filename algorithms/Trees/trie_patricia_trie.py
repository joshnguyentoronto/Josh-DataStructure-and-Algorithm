"""
Patricia trie is build on top of the 'trie'
it try to build the way that save the most space

Like example in 'trie.py':
    storing 'josh' and 'john'
    instead storing   j -> o -> s -> h
                                h -> n
    patricia trie store:  jo -> s -> h
                                h -> n

However if we insert new string 'jazz'
    it has to break out 'jo' to 'j' -> 'o'
    so that when insert 'jazz' it can reuse 'j' and create new 'azz'
The same, it has to break 'azz' in 'jazz' to j-a-zz if we insert 'j-a-smine'



Pros:
    Save more storage than 'trie'
Cons:
    Insert new data can be more difficult
"""