"""
Trees is a sub-set of graph

Characteristic:
    Tree needs a root
    Parent Node can have many Children
    Children should have 'only' one parent
    ( a LinkedList is also a tree, with each node has just 1 child )

Binary Trees is a Tree:
    Each parent Node have max '2' children

Binary Search Trees is a Binary Tree:
    Each Node is ordered from left to right
    The Node will 'bigger' than the 'left sub-tree' and 'smaller' than the 'right sub-tree'
    And that Node will 'bigger' than the 'left' child and 'smaller' than the 'right' child

Heap / Priority Queue is a Binary Tree:
    Max Heap:
        Each parent is bigger than its children
        The root is the biggest value
    Min Heap:
        Each parent is smaller than its children
        The root is the smallest
"""