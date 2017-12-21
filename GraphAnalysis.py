# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack
        print(stack)
        return stack

g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Following is a Topological Sort of the given graph")
TSN = g.topologicalSort()
print(g.graph)


def mapTopologicalStack():
    mapOfNodes = {}
    count = 0
    for nodes in TSN:
        mapOfNodes[nodes] = count
        count += 1
    print(mapOfNodes)
    return mapOfNodes

edgeWeights = []
for k,v in  g.graph.items():
    if v != []:
        edgeWeight = {}
        for vertices in v:
            edgeWeight[vertices] = 1
        try:
            edgeWeights.append(edgeWeight)
        except:
            edgeWeights = [edgeWeight]
print(edgeWeights)

#edgeWeigths = [{1:5,2:3},{2:2,3:6},{3:7,4:4,5:2},{4:-1,5:1},{5:-2}]
def longestDistance():
    nodeValues = {0:0,1:-1000,2:-1000,3:-1000,4:-1000,5:-1000}
    for node in range(4):
        for keys in edgeWeights[node].keys():
            nodeVal = nodeValues[node]
            edgeWt = edgeWeights[node][keys]
            newNodeVal = nodeVal + edgeWt
            if nodeValues[keys] < newNodeVal:
                nodeValues[keys] = newNodeVal
    print(nodeValues)




longestDistance()



