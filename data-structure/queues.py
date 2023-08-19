"""
FIFO: first in first out
can be implement by array or linked list
2 mayor operations is push to bottom and pop the first item

Implement by Array(List)
straight array: enqueue O(1)
                dequeue O(n) with n is the length of the queue
round array enqueue O(1)
            dequeue O(1)

"""



"""
Implement by Linked List
"""
class LinkedList:
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
            nodes.insert(0, 'start queue')
            nodes.append('end queue')
            return ' -> '.join(nodes)

class Node: 
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return self.data

myqueue = LinkedList()

# add to queue (enqueue)
def enqueue(list, data):
    new = Node(data=data)
    if list.count == 0:
        list.head = new
        list.tail = new
    elif list.count >= 1:
        list.tail.next = new
        list.tail = new
    list.count += 1
    return list

print(myqueue)
print(enqueue(myqueue, 2))
print(enqueue(myqueue, 4))
print(enqueue(myqueue, 6))
print(enqueue(myqueue, 8))

# remove from queue (dequeue)
def dequeue(list):
    while list.head is not None:
        value = list.head.data
        list.head = list.head.next
        list.count -= 1
        return value
    return 'queue is empty'

print(dequeue(myqueue))
print(myqueue)
print(dequeue(myqueue))
print(myqueue)
print(dequeue(myqueue))
print(myqueue)
print(dequeue(myqueue))
print(myqueue)


"""
Implement by Array(List)
"""

# Round Array
class ListQueue:
    def __init__(self, size):
        self.arr = [None] * size
        self.front = 0
        self.end = 0
        self.count = 0
        self.size = size
    def __repr__(self):
        array = []
        for i in range(len(self.arr)):
            array.append(str(self.arr[i]))
        return ', '.join(array) + '\nfront is ' + str(self.front) + ', end is ' + str(self.end)

arr_queue = ListQueue(10)
print(arr_queue)

# Enqueue
def arr_enqueue(queue, value):
    if queue.count == queue.size:
        print('queue is full')
        return queue
    elif queue.count == 0:
        queue.arr[queue.front] = value
        queue.count += 1
    elif queue.end == queue.size - 1:
        queue.arr[0] = value
        queue.end = 0
        queue.count += 1
    else:
        queue.arr[queue.end + 1] = value
        queue.end += 1
        queue.count += 1
    
    return queue

print(arr_enqueue(arr_queue, 4))
print(arr_enqueue(arr_queue, 36))
print(arr_enqueue(arr_queue, 12))
print(arr_enqueue(arr_queue, 83))
print(arr_enqueue(arr_queue, 8))
print(arr_enqueue(arr_queue, 52))
print(arr_enqueue(arr_queue, 31))
print(arr_enqueue(arr_queue, 7))
print(arr_enqueue(arr_queue, 99))
print(arr_enqueue(arr_queue, 62))
print(arr_enqueue(arr_queue, 74))


# Dequeue
def arr_dequeue(queue):
    if queue.count == 0:
        return ('queue is empty')
    else:
        value = queue.arr[queue.front]
        queue.arr[queue.front] = None
        if queue.front == queue.size - 1 and queue.count > 1:
            queue.front = 0
        elif queue.count != 1:
            queue.front += 1
        queue.count -= 1
        return value

print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)


print(arr_enqueue(arr_queue, 45))
print(arr_enqueue(arr_queue, 51))
print(arr_enqueue(arr_queue, 23))
print(arr_enqueue(arr_queue, 86))
print(arr_enqueue(arr_queue, 34))
print(arr_enqueue(arr_queue, 98))
print(arr_enqueue(arr_queue, 74))
print(arr_enqueue(arr_queue, 2))
print(arr_enqueue(arr_queue, 8))
print(arr_enqueue(arr_queue, 42))
print(arr_enqueue(arr_queue, 13))


print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)
print(arr_dequeue(arr_queue))
print(arr_queue)


