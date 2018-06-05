from graph_tool.all import *
from SCCFinder import SCCFinder
from main import create_graph, N, M

graph = create_graph(N, M)
scc_finder = SCCFinder(graph)
SCCs = scc_finder.execute()
comp, hist = label_components(graph)

def test_size():
    assert len(hist) == len(SCCs)

def test_label():
    # Extract indeces from vertices of SCCs from our algorithm
    SCCs_indeces = map(lambda SCC: [int(v) for v in SCC], SCCs)
    test_scc = set()
    for scc in SCCs_indeces:
        test_scc.add(frozenset(scc))

    # Extract SCCs from labels coming from graph-tool algorithm
    true_scc_dict = dict.fromkeys(list(set(comp.a)), None)
    for i, x in enumerate(comp.a):
        if true_scc_dict[x] is None:
            true_scc_dict[x] = [i]
        else:
            true_scc_dict[x].append(i)

    # From dictionary to set
    true_scc = set()
    for scc in true_scc_dict.values():
        true_scc.add(frozenset(scc))

    for scc in true_scc:
        assert scc in test_scc

