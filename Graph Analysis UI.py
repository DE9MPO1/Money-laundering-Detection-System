from tkinter import *
import GraphAnalysis as ga

def getGraphAnalysisResults():
    edgeList = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (7, 8), (8, 9), (8, 10),
                (9, 10)]
    g = ga.initializeGraph(edgeList)
    graph = ga.gg.generateGraph(edgeList)
    vertices = ga.gg.getVertices(edgeList)
    indegreeMap = ga.gg.getIndegree(vertices, graph)
    outdegreeMap = ga.gg.getOutDegree(vertices, graph)

    # Getting the sourceNodes
    sourceNodes = ga.dg.getSourceNodes(indegreeMap)
    #inserting sourceNodes into the list
    print("Source Nodes ID from Mapped transactions : ")
    customerList = ga.getCustomerId(sourceNodes)
    for customer in customerList :
        print(customer)
        list2.insert(END,str(customer) + "\n")

    #Inserting destNodes into the list
    print("Destination Nodes ID from Mapped transactions : ")
    destNodes = ga.dg.getDestNodes(outdegreeMap)
    customerList = ga.getCustomerId(destNodes)
    for customer in customerList:
        print(customer)
        list3.insert(END, str(customer) + "\n")

    newEdgeList = ga.dg.splitEdgeList(edgeList, graph, sourceNodes)

    print("Vertex Set after splitting")
    vertexSet = []
    count = 0
    for edgeList in newEdgeList:
        try:
            vertexSet.append(ga.dg.depthFirstSearch(edgeList, graph, sourceNodes[count]))
        except:
            vertexSet = [ga.dg.depthFirstSearch(edgeList, graph, sourceNodes[count])]
        count += 1

    print("New Node Values after splitting")
    newNodeValues = []
    count = 0
    for vertices in vertexSet:
        try:
            newNodeValues.append(ga.gg.genNodeValues(vertices, sourceNodes[count]))
        except:
            newNodeValues = [ga.gg.genNodeValues(vertices, sourceNodes[count])]
        count += 1

    count = 0
    for edgeList in newEdgeList:
        transactInfo = ga.getTransactionInformation(edgeList)
        for transactions in transactInfo:
            for k,v in transactions.items():
                list1.insert(END, str(k) + " "  + str(v))
            list1.insert(END,"\n")

        g = ga.initializeGraph(edgeList)
        g.topologicalSort()
        mapOfNodes = ga.mapTopologicalStack(g)
        ga.longestDistance(newNodeValues[count], mapOfNodes, g)
        count += 1

    print("Longest Path for dest = %d and source = %d" % (10, 7))
    longestPath = ga.getlongestPath({8: [7, 8], 9: [8, 9], 10: [9, 10]}, 10, 7)
    ga.getTransactionInformation(longestPath)

    print("Longest Path for dest = %d and source = %d" % (6, 1))
    longestPath = ga.getlongestPath({2: [1, 2], 3: [2, 3], 4: [3, 4], 5: [4, 5], 6: [5, 6]}, 6, 1)
    ga.getTransactionInformation(longestPath)


window = Tk()
window.geometry("600x1000")

l4 = Label(window,text = "Graphs : ")
l4.grid(row = 0, column = 0,columnspan = 2,pady = 5,padx = 20)
list1 = Listbox(window,width = 40,height = 10)
list1.grid(row = 0,column = 2,columnspan=2,pady = 5,padx = 20)
sb1 = Scrollbar(window)
sb1.grid(row = 0,column = 4, rowspan = 5,pady = 5)

l5 = Label(window,text = "Agents : ")
l5.grid(row = 1, column = 0,columnspan = 2,pady = 5,padx = 20)
list2 = Listbox(window,width = 40,height = 5)
list2.grid(row = 1,column = 2,columnspan=2,pady = 5,padx = 20)
#sb2 = Scrollbar(topFrame)
#sb2.grid(row = 2,column = 9, rowspan = 5,pady = 5)

l6 = Label(window,text = "Integrators : ")
l6.grid(row = 2, column = 0,columnspan = 2,pady = 5,padx = 20)
list3 = Listbox(window,width = 40,height = 5)
list3.grid(row = 2,column = 2,columnspan=2,pady = 5,padx = 20)
#sb3 = Scrollbar(topFrame)
#sb3.grid(row = 3,column = 9, rowspan = 5,pady = 5)

l7 = Label(window,text = "Graph Analysis Result : ")
l7.grid(row = 3, column = 0,columnspan = 2,pady = 5,padx = 20)
list4 = Listbox(window,width = 40,height = 10)
list4.grid(row = 3,column = 2,columnspan=2,pady = 5,padx = 20)

button1 = Button(window, text = "Get Graph Analysis Result",command = getGraphAnalysisResults)
button1.grid(row = 4,column = 2,columnspan = 2,pady = 5,padx = 20)

window.title("Graph Analysis")
window.mainloop()