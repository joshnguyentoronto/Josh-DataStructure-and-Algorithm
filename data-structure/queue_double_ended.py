"""
Double Ended Queue (Deque)
    Enqueue and dequeue at both end with O(1) time
    The key is to have a previous pointer inside the Node structure of the LinkedList
    (Doubly Linked List)
"""

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        if not nodes:
            return 'list is empty'
        else:
            nodes.insert(0, 'None')
            nodes.append('None')
            return ' <--> '.join(nodes)

class DoublyNode: 
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __repr__(self):
        return self.data


doublyqueue = DoublyLinkedList()


# enqueue at front
def dou_enqueue_at_front(list, data):
    new = DoublyNode(data=data)
    if list.count == 0:
        list.head = new
        list.tail = new
    else:
        new.next = list.head
        list.head.prev = new
        list.head = new
    list.count += 1
    return list

print('enqueue at front:')
print(doublyqueue)
print(dou_enqueue_at_front(doublyqueue, 2))
print(dou_enqueue_at_front(doublyqueue, 4))
print(dou_enqueue_at_front(doublyqueue, 6))
print(dou_enqueue_at_front(doublyqueue, 8))



# dequeue at front
def dou_dequeue_at_front(list):
    while list.head is not None:
        value = list.head.data
        list.head = list.head.next
        list.head.prev = None
        list.count -= 1
        return value
    return 'queue is empty'

print('dequeue at front:')
print(dou_dequeue_at_front(doublyqueue))
print(doublyqueue)
print(dou_dequeue_at_front(doublyqueue))
print(doublyqueue)



# enqueue at the back
def dou_enqueue_at_back(list, data):
    new = DoublyNode(data=data)
    if list.count == 0:
        list.head = new
        list.tail = new
    else:
        list.tail.next = new
        new.prev = list.tail
        list.tail = new
    list.count += 1
    return list

print('enqueue at back:')
print(doublyqueue)
print(dou_enqueue_at_back(doublyqueue, 3))
print(dou_enqueue_at_back(doublyqueue, 5))
print(dou_enqueue_at_back(doublyqueue, 7))
print(dou_enqueue_at_back(doublyqueue, 9))



# dequeue at the back
def dou_dequeue_at_back(list):
    while list.tail is not None:
        value = list.tail.data
        list.tail = list.tail.prev
        list.tail.next = None
        list.count -= 1
        return value
    return 'queue is empty'

print('dequeue at back:')
print(dou_dequeue_at_back(doublyqueue))
print(doublyqueue)
print(dou_dequeue_at_back(doublyqueue))
print(doublyqueue)