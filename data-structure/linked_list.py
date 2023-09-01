"""
Operation that we can perform from a Linked List:
    - Get the nth element of the list
    - Search for a value in the list
    - Remove an element by its value
    - Insert an element at the front
    - Insert an element at the back
    - Remove an element at the front
    - Remove an element at the back
"""

# asdf

"""
Create Linked List
___repr___ to print(return the information we need)
"""
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)


"""
Create a Node for Linked List
___repr___ to print(return the information we need)
"""
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return self.data




# create new list
mylist = LinkedList()
print(mylist)
print('-----------------------------')
# create a new node
node1 = Node('apple')
print(node1)
print('-----------------------------')
# cause the linkedlist is empty, we assign node1 to the head of linkedlist
mylist.head = node1
mylist.length += 1
mylist.tail = node1
print(mylist)
print('-----------------------------')



# create more node and link it with the previous node
node2 = Node('banana')
node1.next = node2
mylist.length += 1
mylist.tail = node2

node3 = Node('cherry')
node2.next = node3
mylist.length += 1
mylist.tail = node3

node4 = Node('dragon fruit')
node3.next = node4
mylist.length += 1
mylist.tail = node4

node5 = Node('eggplant')
node4.next = node5
mylist.length += 1
mylist.tail = node5

node6 = Node('fif')
node5.next = node6
mylist.length += 1
mylist.tail = node6
print(mylist)
print('-----------------------------')



# Get the value of the nth element in the list
def get_item(head, nth):
    count = 0
    current = head
    while current is not None:
        if count == nth:
            return current.data
        # print(current)
        current = current.next
        count += 1

fruit1 = get_item(node1, 2)
print('get 2th element in list')
print(fruit1)
print('-----------------------------')



# Search for a value in the list
def search(head, value):
    count = 0
    current = head
    while current is not None:
        if current.data == value:
            return count
        count += 1
        current = current.next

index = search(node1, 'dragon fruit')
print('find index of item by value (dragon fruit)')
print(index)
print('-----------------------------')



# Remove an element by its value
def remove_by_value(head, value):
    prev = head
    current = head
# in case if the value is the head of linked list
    if current.data == value:
        mylist.head = current.next
        current = None
        return mylist
    while current is not None:
        if current.data == value:
            prev.next = current.next
            mylist.length -= 1
            if current.next is None:
                mylist.tail = prev
            current = None
            return mylist
        prev = current
        current = current.next

print('remove an element by its value')
print(mylist)
print(remove_by_value(node1, 'cherry'))
print('-----------------------------')


# Insert an element at the front
def insert_front(head, value):
    new_node = Node(value, next = head)
    mylist.head = new_node
    mylist.length += 1
    return mylist

print('Insert an element at the front')
print(mylist)
insert_front(node1, 'bla bla')
print(mylist)
print('-----------------------------')



# Insert an element at the back
def insert_back(linkedlist, value):
    new_node = Node(value, None)
    linkedlist.tail.next = new_node
    linkedlist.tail = new_node
    linkedlist.length += 1
    return linkedlist

print('Insert an element at the back')
print(mylist)
print(mylist.head)
print(mylist.length)
print(mylist.tail)
print(insert_back(mylist, 'oranges'))
print(mylist.head)
print(mylist.length)
print(mylist.tail)
print('-----------------------------')


# Remove an element at the front
def remove_front(head):
    mylist.head = head.next
    mylist.length -= 1
    head = None
    return mylist

print('remove an element at the front')
print(mylist)
remove_front(node1)
print(mylist)
print('-----------------------------')


# Remove an element at the back
def remove_back(linkedlist):
    current = linkedlist.head
    count = 0
    if linkedlist.length == 0 or linkedlist.length == 1:
        linkedlist.head = linkedlist.tail = None
        linkedlist.length = 0
        return None
    while current is not None:
        if count == linkedlist.length - 2:
            linkedlist.tail = None
            linkedlist.tail = current
            current.next = None
            linkedlist.length -= 1
            return linkedlist
        count += 1
        current = current.next

print('remove an element at the back')
print(mylist)
print(remove_back(mylist))
print(mylist.head)
print(mylist.length)
print(mylist.tail)
print('-----------------------------')


