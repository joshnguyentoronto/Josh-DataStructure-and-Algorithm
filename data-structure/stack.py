"""
LIFO: last in first out

can be implement by array or linked list

2 mayor operations is push and pop
"""

class LinkedList:
    def __init__(self):
        self.head = None
        self.num = 0
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('bottom')
        return ' -> '.join(nodes)

class Node: 
    def __init__(self, data=0, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return self.data


mystack = LinkedList()

# push to linkedlist
def add_to_stack(list, data):
    new_node = Node(data)
    new_node.next = list.head
    list.head = new_node
    list.num += 1
    return list


add_to_stack(mystack, 3)
add_to_stack(mystack, 7)
add_to_stack(mystack, 4)
add_to_stack(mystack, 8)
print(mystack)

# pop an item
def pop_an_item(list):
    if list.head is not None:
        list.num -= 1
        value = list.head.data
        list.head = list.head.next
        return value

print(mystack)
value = pop_an_item(mystack)
print(value)
print(mystack)
