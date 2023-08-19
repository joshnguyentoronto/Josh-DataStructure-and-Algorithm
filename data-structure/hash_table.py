"""
In Python, Dict data structure is a hash table

{ O(1) }
Main Operation:
    Insert a key-value pair
    Delete
    Look up

Hashing - Hash Function:
    Take in an input an return a set of output that easily stored 
    Ex: turn No 0-100 to key of No 0-9

Hashing will create collision, ways to fix this problem:
    Chaining
        Insert {O(1)}
        Look up {O(1 + n/m)}
        Delete {O(1 + n/m)}  
            Bucket size = No Keys(n) / No Slots(m)
            It only possible if the Hashing can return a uniform output
            But over the time, No of Keys may increate and each bucket size increase by a lot,
            we may need to ReHashing to add more slots to optimize the Hash Table
        Re-Hashing take {O(n+m)} but it not happen often so we can ignore it
    Open Addressing
    Probe Sequence
    Cuckoo Hashing


"""

# my_car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(my_car)
# print(my_car["year"])


class HashChaining:
    def __init__(self, slot=0):
        self.table = [None] * slot
        self.slot = slot
        # To keep track when to Re-hashing
        self.track = [0] * slot
        self.max = slot * 2
    def __repr__(self):
        arr = []
        for i in range(len(self.table)):
            arr.append(str(self.table[i]))
        return '\n'.join(arr)

class HashNode: 
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
    def __repr__(self):
        return 'key: ' + str(self.key) + ', value: ' + str(self.value)


def create_table(n):
    newtable = HashChaining(n)
    return newtable

def hashing(string, slot):
    temp = 0
    for c in string:
        temp += ord(c)
    return temp % slot

def insert(table, value):
    key = hashing(value, table.slot)
    new_node = HashNode(key, value)
    new_node.next = table.table[key]
    table.table[key] = new_node
    # Check if there's too much node in one slot
    table.track[key] += 1
    if table.track[key] >= table.max:
        table = rehashing(table)
    return table


def look_up(table, value):
    key = hashing(value, table.slot)
    node = table.table[key]
    pos = 0
    while node is not None:
        if node.value == value:
            return 'name ' + node.value + ' has key: ' + str(key) + ', and at the ' + str(pos) + ' position'
        else:
            pos += 1
            node = node.next
    return 'cannot find name: ' + value



def delete(table, value):
    key = hashing(value, table.slot)
    node = table.table[key]
    prev_node = node
    pos = 0
    while node is not None:
        if node.value == value and pos == 0:
            table.table[key] = node.next
            text = 'Successful delete name: ' + value + ', at slot: ' + str(key) + ', at pos: ' + str(pos)
            node = None
            table.track[key] -= 1
            return text
        elif node.value == value:
            prev_node.next = node.next
            text = 'Successful delete name: ' + value + ', at slot: ' + str(key) + ', at pos: ' + str(pos)
            node = None
            table.track[key] -= 1
            return text
        else:
            pos += 1
            prev_node = node
            node = node.next
    return "Name " + value + ' not found, cannot operate delete!'

hash_chaining_table = create_table(10)
# print(hash_chaining_table)
insert(hash_chaining_table, 'Josh')
insert(hash_chaining_table, 'Clara')
insert(hash_chaining_table, 'Jim')
insert(hash_chaining_table, 'Tim')
insert(hash_chaining_table, 'Layla')
insert(hash_chaining_table, 'Joanne')
insert(hash_chaining_table, 'Andrei')

print("==================")
print(hash_chaining_table)

print("==================")
print(look_up(hash_chaining_table, 'Josh'))
print(look_up(hash_chaining_table, 'Jim'))
print(look_up(hash_chaining_table, 'Tim'))
print(look_up(hash_chaining_table, 'tim'))

print("==================")
print(delete(hash_chaining_table, 'alsf'))
print(delete(hash_chaining_table, 'Layla'))

print(look_up(hash_chaining_table, 'Tim'))
print(delete(hash_chaining_table, 'Tim'))
print(look_up(hash_chaining_table, 'Tim'))
print("==================")
print(hash_chaining_table)




"""
Re-Hashing
    When No of Keys increate and each bucket size increase by a lot compare to No of Slots,
    we may need to ReHashing to add more slots to optimize the Hash Table
Re-Hashing take {O(n+m)} but it not happen often so we can ignore it

Let's try Re-hashing when one of the slot has Number of Keys 'double' the size of Slots
There are two way we can monitor this:
    when the average of key/slot double the size of slots (not good if our hashing function isn't good and most of the key end up in few slot)
    or keep track each slot with a seperate array (more accurate re-hashing 'if' we have sophisticated hashing function but bat value input)
"""

def rehashing(table):
    new_table = create_table(table.slot*2)
    for i in range(len(table.table)):
        node = table.table[i]
        while node is not None:
            insert(new_table, node.value)
            node = node.next
    table = new_table
    return table

rehashing_table = rehashing(hash_chaining_table)
print("==================")
print(rehashing_table)
