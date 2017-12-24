# Python program to print topological sorting of a DAG
from collections import defaultdict
import GraphGeneration as gg
import FrequentTransactions as ft
import DisconnectedGraphs as dg

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
        print("Topological Sort")
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


def initializeGraph(edgeList):
    """
        Initializes th graph
        Input : Number of Edges
                Edges in the form of tuple
        Output: returns graph object
    """
    g = Graph(len(edgeList))
    for edges in edgeList:
        g.addEdge(edges[0],edges[1])
    #print(g.graph)
    return g


def mapTopologicalStack(g):
    """
        Maps the vertices/nodes of the topologically sorted graph
        Input : vertices of the graph (3,2,1,0)
        Output : returns map of nodes (3:0,2:1,1:2,0:3)
    """
    print("Mapping Nodes")
    mapOfNodes = {}
    count = 0
    for k,v in g.graph.items():
        mapOfNodes[k] = count
        count += 1
    print(mapOfNodes)
    return mapOfNodes

def genEdgeWeights(g):
    """
            Initializes the edge weights of the graph to one
            Input : [1:[2,3], 2:[3,4], 3:[4,5,6], 4: [5,6], 5:[6]]
                    Here key is the vertex of the graph
                    and Value is a list of vertices to which the key vertex is connected,
                    forming an edge.
            Output : [{2: 1, 3: 1}, {3: 1, 4: 1}, {4: 1, 5: 1, 6: 1}, {5: 1, 6: 1}, {6: 1}]
    """
    print("Assigning Edge Weights  ")
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
    return edgeWeights

def longestDistance(nodeValues,mapOfNodes,g):
    """
    Description : Finds the Longest Distance between source Nodes and other Nodes in the graph
          Input : nodeValues = {1:0,2:-1000,3:-1000,4:-1000,5:-1000,6:-1000}
                  g = [1:[2,3], 2:[3,4], 3:[4,5,6], 4: [5,6], 5:[6]]
                  edgeWeights = [{2: 1, 3: 1}, {3: 1, 4: 1}, {4: 1, 5: 1, 6: 1}, {5: 1, 6: 1}, {6: 1}]
         Output : nodeValues = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}}
    """
    edgeWeights = genEdgeWeights(g)
    print(edgeWeights)

    print("Longest Distance Function : ")
    #print("len ",len(nodeValues.keys()))
    for node in nodeValues.keys():
        try:
            #print(edgeWeights[mapOfNodes[node]])
            for key in edgeWeights[mapOfNodes[node]].keys():
                nodeVal = nodeValues[node] #0
                edgeWt = edgeWeights[mapOfNodes[node]][key] #eW[4][2] = 1
                newNodeVal = nodeVal + edgeWt #1
                if nodeValues[key] < newNodeVal:
                    nodeValues[key] = newNodeVal
        except:
            print("Exception!!!")
    print(nodeValues)

print("Tuple List")
tupleList = ft.mapCustomers()
print("Total Number of Transactions : ",len(tupleList))

print("Actual Frequency of Transactions : ")
actualTransFreq = ft.actualCount(tupleList)

print("Hash Based Bucket Count : ")
bucketContainer = ft.hashBasedBucketCount(tupleList)

print("Filtered transactions(On Basis of Bucket Count) : ")
filteredBucketTuples = ft.filterOnBucketCount(tupleList,bucketContainer,120)

print("Filtered Transactions(On Basis of actual Frequency) : ")
actualCount = ft.filterOnActualCount(filteredBucketTuples,actualTransFreq,0)
print(actualCount)



#edgeList = []
#for keys in actualCount.keys():
#    try:
#        edgeList.append(keys)
#   except:
#        edgeList = [keys]


def main():

    edgeList = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6),(7,8),(8,9),(8,10),(9,10)]
    print("Edge List")
    print(edgeList)

    g = initializeGraph(edgeList)
    graph = gg.generateGraph(edgeList)
    vertices = gg.getVertices(edgeList)
    indegreeMap = gg.getIndegree(vertices,graph)
    outdegreeMap = gg.getOutDegree(vertices,graph)


    #Getting the sourceNodes
    sourceNodes = dg.getSourceNodes(indegreeMap)
    newEdgeList = dg.splitEdgeList(edgeList,graph,sourceNodes)


    print("Vertex Set after splitting")
    vertexSet = []
    count = 0
    for edgeList in newEdgeList:
        try:
            vertexSet.append(dg.depthFirstSearch(edgeList,graph,sourceNodes[count]))
        except:
            vertexSet = [dg.depthFirstSearch(edgeList,graph,sourceNodes[count])]
        count += 1

    print("New Node Values after splitting")
    newNodeValues = []
    count = 0
    for vertices in vertexSet:
        try:
            newNodeValues.append(gg.genNodeValues(vertices,sourceNodes[count]))
        except:
            newNodeValues = [gg.genNodeValues(vertices,sourceNodes[count])]
        count += 1

    count = 0
    for edgeList in newEdgeList:
        print("Edge List")
        print(edgeList)
        g = initializeGraph(edgeList)
        g.topologicalSort()
        mapOfNodes = mapTopologicalStack(g)
        longestDistance(newNodeValues[count],mapOfNodes,g)
        count += 1


main()