
def generateGraph(tupleList):
    graph = {}
    for tuple in tupleList:
        if tuple[0] not in graph.keys():
            graph[tuple[0]] = [tuple[1]]
        else:
            graph[tuple[0]].append(tuple[1])
    print(graph)

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

edgeList = [(5,6),(3,5),(3,6),(2,3),(4,5),(1,2),(3,4)]
generateGraph(edgeList)
getVertices(edgeList)