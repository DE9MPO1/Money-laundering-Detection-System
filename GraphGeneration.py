
def generateGraph(tupleList):
    graph = {}
    for tuple in tupleList:
        if tuple[0] not in graph.keys():
            graph[tuple[0]] = [tuple[1]]
        else:
            graph[tuple[0]].append(tuple[1])
    print(graph)
    return graph

def getVertices(tupleList):
    vertices = []
    for tuple in tupleList:
        if tuple[0] not in vertices:
            try:
                vertices.append(tuple[0])
            except:
                vertices = [tuple[0]]
        if tuple[1] not in vertices:
                vertices.append(tuple[1])
    vertices.sort()
    #print(vertices)
    return vertices

def getIndegree(vertices,graph):
    indegreeMap = {}
    for node in vertices:
        count = 0
        for keys in graph.keys():
            if node in graph[keys]:
                #print(node,graph[keys])
                count += 1
        indegreeMap[node] = count
    #print(indegreeMap)
    #print("Returns a map of indegree of each Node")
    return indegreeMap

def getOutDegree(vertices,graph):
    outDegreeMap = {}
    for node in vertices:
        if node in graph.keys():
            print(node,len(graph[node]))
            outDegreeMap[node] = len(graph[node])
        else:
            outDegreeMap[node] = 0
    print(outDegreeMap)

edgeList = [(5,6),(3,5),(3,6),(2,3),(4,5),(1,2),(3,4)]
graph = generateGraph(edgeList)
vertices = getVertices(edgeList)
getIndegree(vertices,graph)
getOutDegree(vertices,graph)