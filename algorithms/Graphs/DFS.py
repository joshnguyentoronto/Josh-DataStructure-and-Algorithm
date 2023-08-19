"""
From the Source Node
Go As Deep As Possible 
Until there is no more node, 
Retrace the step to find more node

The process of Discovering and Finishing

The Key to DFS is to use a Stack to store vertices that have been discovered
Each Vertex we discovered is added to the Stack
and instead finishing that node, we discover the new node that added to the stack
Once there's no more edges to discover in that vertex, we mark them as Finished and remove from the Stack
Then we continue with another node in the stack

Also we mark the vertices when we discover them to avoid endless discovering

Time Complexity: { O(|V| + |E|) }
Space Complexity: { O(|V|) }

"""







"""
Get from the BFS.py
Let's represent a connection between 5 people: 
    Josh: Clara, Joma, Kay, Kim
    Clara: Josh, Tim, Kay, Kim
    Tim: Clara, Joma, Steven, Jane
    Joma: Josh, Tim, Jane
    Kay: Josh, Clara, Steven
    Kim: Josh, Clara, Steven
    Steven: Tim, Kay, Kim, Jane
    Jane: Joma, Tim, Steven
There're no weight in the connection and connection is mutual so undirected
"""

# It's a Graph but also a Hash Map
class Graph:
    def __init__(self, slot):
        self.table = [None] * slot
        self.slot = slot
        # To keep track when to Re-hashing, we will ignore this for now
        self.track = [0] * slot
        self.max = slot * 2
    def __repr__(self):
        arr = []
        for i in range(len(self.table)):
            arr.append(str(self.table[i]))
        return '\n'.join(arr)

class Vertex:
    def __init__(self, key, name, next=None):
        # Key to easily find in the hash table
        self.key = key
        self.name = name
        # array of pointers to other people (vertices)
        # Or it can be a LinkedList
        self.edges = []
        # Point to the next person in the hash table
        self.next = next
        self.stacknext = None
        self.discovered = False
    def __repr__(self):
        names = []
        for i in range(len(self.edges)):
            names.append(self.edges[i].name)
        return self.name + ' is connected to: ' + ', '.join(names)

def create_graph(slot):
    new = Graph(slot)
    return new

def hashing(name, slot):
    n = 0
    for char in name:
        n += ord(char)
    return n % slot

# Ignore this for now
def rehashing():
    return

def create_people(graph, name):
    key = hashing(name, graph.slot)
    new = Vertex(key, name)
    new.next = graph.table[key]
    graph.table[key] = new
    # Check if there's too much node in one slot to rehashing
    # graph.track[key] += 1
    # if graph.track[key] >= graph.max:
    #     graph = rehashing(graph)
    return new

def look_up(graph, name):
    key = hashing(name, graph.slot)
    node = graph.table[key]
    while node is not None:
        if name == node.name:
            return node
        else:
            node = node.next
    return False

# Mutual connection - Undirected Graph so add to each other
def add_connection(graph, root, name):
    node1 = look_up(graph, root)
    node2 = look_up(graph, name)
    if node1 and node2 is not False:
        node1.edges.append(node2)
        node2.edges.append(node1)
        return [node1, node2]
    return False

def delete_people(graph, name):
    key = hashing(name, graph.slot)
    node = graph.table[key]
    pre_node = graph.table[key]
    pos = 0
    while node is not None:
        if name == node.name and pos == 0:
            for i in range(len(node.edges)):
                other = look_up(graph, node.edges[i].name)
                if other is not False:
                    store_f = 0
                    for f in range(len(other.edges)):
                        if other.edges[f].name == node.name:
                            store_f = f
                    other.edges.pop(store_f)
            graph.table[key] = node.next
            node = None
            return graph
        elif name == node.name:
            for i in range(len(node.edges)):
                other = look_up(graph, node.edges[i].name)
                if other is not False:
                    store_f = 0
                    for f in range(len(other.edges)):
                        if other.edges[f].name == node.name:
                            store_f = f
                    other.edges.pop(store_f)
            pre_node.next = node.next
            node = None
            return graph
        else:
            pos += 1
            pre_node = node
            node = node.next
    return 'cannot delete ' + name

def delete_connection(graph, root, name):
    node1 = look_up(graph, root)
    node2 = look_up(graph, name)
    if node1 and node2 is not False:
        store_i = 0
        for i in range(len(node1.edges)):
            if node1.edges[i].name == node2.name:
                store_i = i
        node1.edges.pop(store_i)

        store_f = 0
        for f in range(len(node2.edges)):
            if node2.edges[f].name == node1.name:
                store_f = f
        node2.edges.pop(store_f)
    return [node1, node2]



"""
0: Josh: Clara, Joma, Kay, Kim
1: Clara: Josh, Tim, Kay, Kim
2: Tim: Clara, Joma, Steven, Jane
3: Joma: Josh, Tim, Jane
4: Kay: Josh, Clara, Steven
5: Kim: Josh, Clara, Steven
6: Steven: Tim, Kay, Kim, Jane
7: Jane: Joma, Tim, Steven
"""
mygraph = create_graph(10)
Josh = create_people(mygraph, 'Josh')
Clara = create_people(mygraph, 'Clara')
Tim = create_people(mygraph, 'Tim')
Joma = create_people(mygraph, 'Joma')
Kay = create_people(mygraph, 'Kay')
Kim = create_people(mygraph, 'Kim')
Steven = create_people(mygraph, 'Steven')
Jane = create_people(mygraph, 'Jane')

add_connection(mygraph, 'Josh', 'Clara')
add_connection(mygraph, 'Josh', 'Joma')
add_connection(mygraph, 'Josh', 'Kay')
add_connection(mygraph, 'Clara', 'Tim')
add_connection(mygraph, 'Clara', 'Kay')
add_connection(mygraph, 'Tim', 'Joma')
add_connection(mygraph, 'Kim', 'Josh')
add_connection(mygraph, 'Kim', 'Clara')
add_connection(mygraph, 'Kim', 'Steven')
add_connection(mygraph, 'Steven', 'Tim')
add_connection(mygraph, 'Steven', 'Kay')
add_connection(mygraph, 'Steven', 'Jane')
add_connection(mygraph, 'Jane', 'Joma')
add_connection(mygraph, 'Jane', 'Tim')
print(mygraph)
print(look_up(mygraph,'Clara'))
print(look_up(mygraph,'Kim'))

print('==================')
print('==================')
print('==================')


# Differences
# Differences
# Differences
# Differences
# Differences
# Differences


# Remember to turn all node mark undiscover 
# We don't need to create a stack ADT
# because in this recursive function, when there're an array of edge node,
# the function continue with the new node in the array
# and it finish it first and return finish the other task
def DFS(rootnode):
    rootnode.discovered = True
    for node in rootnode.edges:
        if not node.discovered:
            print(node)
            DFS(node)
    return
print(Josh)

DFS(Josh)