"""
Root node keep the same
Swap the node on the right to the left in every level

"""


class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_tree(node, x):
    if node is None:
        new_node = Node()
        new_node.value = x
        node = new_node
    elif x < node.value:
        node.left = insert_tree(node.left, x)
    elif x > node.value:
        node.right = insert_tree(node.right, x)
    return node

def tree_insert(tree, x):
    tree.root = insert_tree(tree.root, x)

def find_tree(node, x):
    if node is None:
        return "cannot find value " + str(x)
    elif x == node.value:
        return True
    elif x < node.value:
        return find_tree(node.left, x)
    elif x > node.value:
        return find_tree(node.right, x)



def invert_tree(node):
    if not node:
        return
    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)

def print_tree(node, level):
    if not node:
        return
    print('\t' * level + str(node.value))
    level += 1
    print_tree(node.left, level)
    print_tree(node.right, level)


mytree = Tree()
tree_insert(mytree, 9)
tree_insert(mytree, 6)
tree_insert(mytree, 14)
tree_insert(mytree, 4)
tree_insert(mytree, 20)
tree_insert(mytree, 1)
tree_insert(mytree, 3)
tree_insert(mytree, 10)
tree_insert(mytree, 17)
tree_insert(mytree, 2)
tree_insert(mytree, 18)
tree_insert(mytree, 7)
tree_insert(mytree, 8)


print_tree(mytree.root, 0)
print('==============')
invert_tree(mytree.root)
print_tree(mytree.root,0)