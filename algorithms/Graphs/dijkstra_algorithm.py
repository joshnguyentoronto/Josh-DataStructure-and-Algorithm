"""
Dijkstra Algorithm: given a graph and a source vertex (root node), find the shortest path to all other vertices
    (this can simplify to from source vertex, find shortest path to vertex 5)

Implementation:
        first create sptSet set to keep track all vertices included in the spt tree, whose minimum distance from the source is calculated and finalized
        Create boolean array sptSet[] to keep track vertices included in sptSet or not
        Create array dist[] to store shortest distance values of all vertices
        and assign distance to all vertices as {0, inf, inf, inf, inf, inf, inf, inf, inf}
    Pick the vertex with minimum distance value (in this case is the source vertex that we assign distance 0)
        then include it into sptSet = {0}
        then update distance value of its adjacent vertices
    Pick a vertex with minimum distance value (that not already in the sptSet)
        add it to sptSet = {0, 1}
        then update the distance value of its adjacent vertices
    Pick a vertex with minimum distance value (that not already in the sptSet)
        add it to sptSet = {0, 1, 7}
        then update the distance value of its adjacent vertices
    (repeat the step until sptSet include all vertices of the graph)
Shortcut:
    sptSet (or SPT): Shortest Path Tree set
    dist: distance

"""




"""
Dijkstra shortest path algorithm using Prim's Algorithms in O(V^2)
"""
# Library for INT_MAX
import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
        # Initialize minimum distance for next node
        min = sys.maxsize
        # Search not nearest vertex not in the spt
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
            # Update distance value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex is not in the spt
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)


# Undirected Weighted graph
if __name__ == "__main__":
    g = Graph(9)
    g.graph = [ [0,  4,  0,  0,  0,  0,  0,  8,  0],
                [4,  0,  8,  0,  0,  0,  0, 11,  0],
                [0,  8,  0,  7,  0,  4,  0,  0,  2],
                [0,  0,  7,  0,  9, 14,  0,  0,  0],
                [0,  0,  0,  9,  0, 10,  0,  0,  0],
                [0,  0,  4, 14, 10,  0,  2,  0,  0],
                [0,  0,  0,  0,  0,  2,  0,  1,  6],
                [8, 11,  0,  0,  0,  0,  1,  0,  7],
                [0,  0,  2,  0,  0,  0,  6,  7,  0]
    ]
    g.dijkstra(0)

print('========================')

"""
Dijkstra shortest path algorithm using Heap (priority queues) in O( E*Log(V) )
"""
import heapq

# iPair ==> Integer Pair
iPair = tuple

# This class represents a directed graph using
# adjacency list representation
class Graph:
	def __init__(self, V: int):
		self.V = V
		self.adj = [[] for _ in range(V)]
	def addEdge(self, u: int, v: int, w: int):
		self.adj[u].append((v, w))
		self.adj[v].append((u, w))
	# Prints shortest paths from src to all other vertices
	def shortestPath(self, src: int):
		# Create a priority queue to store vertices that
		# are being preprocessed
		pq = []
		heapq.heappush(pq, (0, src))
		# Create a vector for distances and initialize all
		# distances as infinite (INF)
		dist = [float('inf')] * self.V
		dist[src] = 0
		while pq:
			# The first vertex in pair is the minimum distance
			# vertex, extract it from priority queue.
			# vertex label is stored in second of pair
			d, u = heapq.heappop(pq)
			# 'i' is used to get all adjacent vertices of a
			# vertex
			for v, weight in self.adj[u]:
				# If there is shorted path to v through u.
				if dist[v] > dist[u] + weight:
					# Updating distance of v
					dist[v] = dist[u] + weight
					heapq.heappush(pq, (dist[v], v))
		# Print shortest distances stored in dist[]
		for i in range(self.V):
			print(f"{i} \t\t {dist[i]}")

# Driver's code
if __name__ == "__main__":
	# create the graph given in above figure
	V = 9
	g = Graph(V)
	# making above shown graph
	g.addEdge(0, 1, 4)
	g.addEdge(0, 7, 8)
	g.addEdge(1, 2, 8)
	g.addEdge(1, 7, 11)
	g.addEdge(2, 3, 7)
	g.addEdge(2, 8, 2)
	g.addEdge(2, 5, 4)
	g.addEdge(3, 4, 9)
	g.addEdge(3, 5, 14)
	g.addEdge(4, 5, 10)
	g.addEdge(5, 6, 2)
	g.addEdge(6, 7, 1)
	g.addEdge(6, 8, 6)
	g.addEdge(7, 8, 7)

	g.shortestPath(0)
