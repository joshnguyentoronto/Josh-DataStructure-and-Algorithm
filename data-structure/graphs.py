"""
A graph is a set of nodes that are connected by many edges:
    Vertices (V): Nodes
    Edges (E)

G = ( V , E )
V = {v1, v2, v3, v4, v5}
E = {e1, e2, e3, e4, e5, e6, e7, e8}
e1 = ( v1, v2 ) <directed Edge> tuple
e1 = { v1, v2 } <undirected Edge> set

Directed Graphs (Digraph):
Undirected Graphs:
Weighted Graphs:
Unweighted Graphs:


Representation of Graphs:
    Edge List:
    Adjacency Matrices:
    Adjacency List (Most Common)



Graph Problem:
    Find all nodes
    Find all nodes reachable from a vertex
    Find the shortest path from one vertex to another
"""



"""
Edge List
    Time complexity {O(n)}
    Space complexity { < O(n)}
"""
# This represent Un-directed and Un-weighted Graph that have 8 edges
edge_list = [ {0,1}, {0,3}, {0,5}, {1,2}, {1,3}, {2,3}, {3,4}, {4,5} ]

# This represent Directed Graph that have 8 edges and each edge is weighted from 1-4
edge_list = [ (0,1,3), (0,3,2), (0,5,2), (1,2,3), (1,3,2), (2,3,4), (3,4,1), (4,5,4) ]



""" 
Adjacency Matrices 
    Time complexity {O(1)}
    Space complexity {O(n^2)}
* But if want to check 'how many conection a vertex has', it's O(n)
"""
# This represent Un-directed graph
# with 6 vertices (6 row and 6 column)
# 0 = No edge between vertices
# 1 = Vertices connect by an edge
adjacency_matrices = [
    [ 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 1, 1, 0, 0 ],
    [ 0, 1, 0, 1, 0, 0 ],
    [ 1, 1, 1, 0, 1, 0 ],
    [ 0, 0, 0, 1, 0, 1 ],
    [ 1, 0, 0, 0, 1, 0 ]
]

# This represent Directed graph
# Vertex 0 point to v2, v4
# Vertex 5 point to v0 but v0 'not' point to v5
adjacency_matrices = [
    [ 0, 1, 0, 1, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0 ],
    [ 1, 0, 0, 0, 0, 0 ]
]

# This represent Undirected - Weighted Graph
# Number represent weight from 1 vertex to another
adjacency_matrices = [ 
    [0,  4,  0,  0,  0,  0,  0,  8,  0],
    [4,  0,  8,  0,  0,  0,  0, 11,  0],
    [0,  8,  0,  7,  0,  4,  0,  0,  2],
    [0,  0,  7,  0,  9, 14,  0,  0,  0],
    [0,  0,  0,  9,  0, 10,  0,  0,  0],
    [0,  0,  4, 14, 10,  0,  2,  0,  0],
    [0,  0,  0,  0,  0,  2,  0,  1,  6],
    [8, 11,  0,  0,  0,  0,  1,  0,  7],
    [0,  0,  2,  0,  0,  0,  6,  7,  0]
]


""" 
Adjacency List
    Time complexity {O(1) - O(n-1)}  [with n is how many edge a vertex has, worst case it connect to all other vertices other than itself]
    Space complexity {O(n) - O(2n)}
use with array or linkedlist
"""
# This represent Un-directed Graph
# Cause v0 point to v1, v3, v5
# and v1, v3, v5 also point to v0
adjancency_list = [
    [ 1, 3, 5 ],
    [ 0, 2, 3 ],
    [ 1, 3 ],
    [ 0, 1, 2, 4 ],
    [ 3, 5 ],
    [ 0, 4 ],
]
# This represent Un-directed Graph with weight
# In each Tuple first No represent vertices and 2nd No is weight
adjancency_list = [
    [ (1,2), (3,1), (5,3) ],
    [ (0,2), (2,1), (3,1) ],
    [ (1,2), (3,1) ],
    [ (0,2), (1,2), (2,4), (4,1) ],
    [ (3,1), (5,3) ],
    [ (0,2), (4,2) ],
]








"""
Let's represent a connection between 5 people: 
    Josh: Clara, Joma, Kay
    Clara: Josh, Tim, Kay
    Tim: Clara, Joma
    Joma: Josh, Tim
    Kay: Josh, Clara
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


mygraph = create_graph(10)
Josh = create_people(mygraph, 'Josh')
Clara = create_people(mygraph, 'Clara')
Tim = create_people(mygraph, 'Tim')
Joma = create_people(mygraph, 'Joma')
Kay = create_people(mygraph, 'Kay')
print(mygraph)

print('==================')
add_connection(mygraph, 'Josh', 'Clara')
add_connection(mygraph, 'Josh', 'Joma')
add_connection(mygraph, 'Josh', 'Kay')
add_connection(mygraph, 'Clara', 'Tim')
add_connection(mygraph, 'Clara', 'Kay')
add_connection(mygraph, 'Tim', 'Joma')
print(mygraph)
print(look_up(mygraph,'Clara'))

print('==================')
print(delete_connection(mygraph, 'Josh', 'Kay'))
print(mygraph)

print('==================')
print(delete_people(mygraph, 'Kay'))


