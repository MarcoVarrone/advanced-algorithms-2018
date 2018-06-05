class SCCFinder:

    def __init__(self, graph):
        # Initialize private variables
        self.graph = graph

        # Initialize vertices properties.
        # Each vertex has undefined index and lowlink properties equal to -1
        self.indices = graph.new_vertex_property("int", -1)
        self.lowlinks = graph.new_vertex_property("int", -1)
        self.onStack = graph.new_vertex_property("bool", False)
        self.stack = list()
        self.index = 0

        # List that after execution will contain the Strongly Connected Components
        # Each SCC will be represented as a list of vertices.
        self.SCCs = list()

    def execute(self):
        for v in self.graph.vertices():
            if self.indices[v] == -1:
                self.tarjan(v)
        return self.SCCs

    def tarjan(self, v):
        self.indices[v] = self.index
        self.lowlinks[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.onStack[v] = True

        # Get all nodes connected to v by (v, w)
        for w in v.out_neighbors():
            if self.indices[w] == -1:
                self.tarjan(w)
                self.lowlinks[v] = min(self.lowlinks[v], self.lowlinks[w])
            elif self.onStack[w]:
                self.lowlinks[v] = min(self.lowlinks[v], self.indices[w])

        if self.lowlinks[v] == self.indices[v]:
            SCC = list()

            # Replicate the add to the SCC list to simulate a do-while loop
            w = self.add_to_SCC(SCC)
            while w != v:
                w = self.add_to_SCC(SCC)

            self.SCCs.append(SCC)

    def add_to_SCC(self, SCC):
        w = self.stack.pop()
        self.onStack[w] = False
        SCC.append(w)
        return w
