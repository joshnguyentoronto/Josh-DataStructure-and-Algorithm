"""
Suffix tree is data structure that build on top of 'Trie'
    it try to attack the weakness of 'Trie': the difficulty of searching for substring the occur anywhere in the string

It does this simply by create a Patricia trie that not just contain the word
    but also all the suffix in that word
    and along with each of those, we'd store the position of that substring within the overall string
        from which it derived: { {'josh', 0}, {'osh', 1}, {'sh', 2}, {'h', 3} }

This way if we need to look for 'sh'
    we just need to look for it directly with the beginning of substring
    then follow the nodes for the remainder of substring

There is a famous algorithms by 'Ukkonen' for building a suffix tree in O(n) with n:length of string

E.g.:
    for word like 'josh'
        it will store 'josh', 'osh', 'sh', 'h'
    for word like 'abakan'
        it will store 'abakan', 'bakan', 'akan', 'kan', 'an', 'n'
        since it has 3 suffixes start with 'a'
        it will have a tree -> a-> bakan (abakan)
                                -> kan (akan)
                                -> n (an)
                            -> bakan (bakan)
                            -> kan (kan)
                            -> n (n)

Note: Suffix Trie is different to Suffix Tree
    Suffix Trie: don't make use of Patricia Trie and each 'letter' is store in a node
        Space: O(n^2)
    Suffix Tree: use Patricia Trie so each suffix (eg: bakan in abakan) is store in 1 node only
        (because each string has n lenght, so it also has n suffix)
        Space: O(n)

Pros:
    Like Trie find exact match or string start with '...' character
    and Fast substring searching
    This also help to solve many complicated string problem
Cons:
    Store a lot of 'redundant' data -> waste space to optimize time
    Since it's Patricia trie, insert new data is still a pain
    Space: O(2n) -> O(n^2)
"""


