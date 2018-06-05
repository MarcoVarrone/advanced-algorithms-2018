from graph_tool.all import *
from itertools import izip
from numpy.random import randint
from SCCFinder import SCCFinder

# Number of nodes
N = 150
# Number of edges
M = 300

def create_graph(N, M):
    g = Graph()
    # Create a graph of
    g.add_vertex(N)
    # insert some random links
    for s, t in izip(randint(0, N, M), randint(0, N, M)):
        g.add_edge(g.vertex(s), g.vertex(t))
    return g

def draw(graph, colors=None, filename="random-graph.png"):
    graphviz_draw(graph, vcolor=colors, output=filename, ratio="expand", vsize=0.2)
    #graph_draw(graph, vertex_text=graph.vertex_index, output="random-graph.png", bg_color=[1, 1, 1, 1],
    #           output_size=(1000, 1000))

def color_SCC(graph, SCCs):
    # Perform deep copy of graph to prevent side effects
    graph_colored = Graph(graph)
    colors = graph.new_vertex_property('int')

    for i, SCC in enumerate(SCCs):
        color = i*round(255/len(SCCs))
        for vertex in graph_colored.vertices():
            if vertex in SCC:
                colors[vertex] = color
    return graph_colored, colors


graph = create_graph(N, M)
scc_finder = SCCFinder(graph)
SCCs = scc_finder.execute()
graph_colored, colors = color_SCC(graph, SCCs)
draw(graph_colored, colors)

