"""
Trees:
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

    
Main Operation:
    Create BST
    Insert (and maintain order of the BST)

What is a balanced tree???
    left and right subtree height different at most one
    left subtree is balanced
    right subtree is balanced
"""



class BST:
    def __init__(self):
        self.root = None

class BSTNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

mybst = BST()

def insert_BST(node, x):
    if node is None:
        new_node = BSTNode()
        new_node.value = x
        node = new_node
    elif x < node.value:
        node.left = insert_BST(node.left, x)
    elif x > node.value:
        node.right = insert_BST(node.right, x)
    return node

def bst_insert(tree, x):
    tree.root = insert_BST(tree.root, x)

def find_BST(node, x):
    if node is None:
        return "cannot find value " + str(x)
    elif x == node.value:
        return True
    elif x < node.value:
        return find_BST(node.left, x)
    elif x > node.value:
        return find_BST(node.right, x)

bst_insert(mybst, 30)
bst_insert(mybst, 20)
bst_insert(mybst, 40)
bst_insert(mybst, 50)
bst_insert(mybst, 60)

print(find_BST(mybst.root, 30))
print(find_BST(mybst.root, 20))
print(find_BST(mybst.root, 24))
print(find_BST(mybst.root, 60))
print(find_BST(mybst.root, 70))






"""
=============================
Balance a Binary Search Tree:
=============================
"""

# Stort all bst node to a list 
# (store from left to right so that it is order automatically)
def store_node(node, arr):
    if not node:
        return
    # Store from left to right on each level of subtree
    store_node(node.left, arr)
    arr.append(node)
    store_node(node.right, arr)

# Recursive func to construct the binary search tree
def construct_bst(arr, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    node = arr[mid]

    node.left = construct_bst(arr, start, mid-1)
    node.right = construct_bst(arr, mid+1, end)
    return node


def build_bst(bst):
    nodes = []
    store_node(bst.root, nodes)

    node = construct_bst(nodes, 0, len(nodes)-1)
    bst.root = node
    return bst.root