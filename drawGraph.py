import networkx as nx
import matplotlib.pyplot as plt



def drawGraph(edgeList):
    G=nx.Graph()
    # adding a list of edges:
    G.add_edges_from(edgeList)

    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())

    nx.draw_networkx(G)
    plt.savefig("simple_path.png") # save as png
    plt.show() # display

