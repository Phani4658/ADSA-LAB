class Graph:
def __init__(self, vertices):
self.V = vertices # No. of vertices self.graph = []
# function to add an edge to graph def addEdge(self, u, v, w):
self.graph.append([u, v, w])
def find(self, parent, i): if parent[i] == i:
return i
return self.find(parent, parent[i])
# A function that does union of two sets of x and y # (uses union by rank)
def union(self, parent, rank, x, y):
xroot = self.find(parent, x) yroot = self.find(parent, y)
if rank[xroot] < rank[yroot]: parent[xroot] = yroot
elif rank[xroot] > rank[yroot]: parent[yroot] = xroot
# If ranks are same, then make one as root # and increment its rank by one
else:
parent[yroot] = xroot rank[xroot] += 1
def KruskalMST(self):
result = [] # This will store the resultant MST
   24

         # An index variable, used for sorted edges
i= 0
e=0
self.graph = sorted(self.graph,key=lambda item: item[2]) parent = []
rank = []
# Create V subsets with single elements for node in range(self.V):
parent.append(node) rank.append(0)
# Number of edges to be taken is equal to V-1 while e < self.V - 1:
u, v, w = self.graph[i] i = i +1
x = self.find(parent, u) y = self.find(parent, v)
if x != y: e=e+1
result.append([u, v, w]) self.union(parent, rank, x, y)
minimumCost = 0
print ("Edges in the constructed MST") for u, v, weight in result:
minimumCost += weight
print("%d -- %d == %d" % (u, v, weight)) print("Minimum Spanning Tree" , minimumCost)
g = Graph(7) g.addEdge(0, g.addEdge(0, g.addEdge(1, g.addEdge(1, g.addEdge(2, g.addEdge(3, g.addEdge(3, g.addEdge(4, g.addEdge(4, g.KruskalMST()
1, 28) 5, 10) 2, 16) 6, 14) 3, 12) 4, 22) 6, 18) 5, 25) 6, 24)
