from collections import defaultdict
from searchviz.ipy_graph_display import Step


def BFS_search(G, start_node):
    steps = []
    parent_mapping = defaultdict(lambda: None)
    visited = defaultdict(lambda: False)
    visited[start_node] = True
    q = [start_node]
    steps.append(Step(nodes=["A"], type="start"))
    while len(q) > 0:
        current = q.pop()
        steps.append(Step([current], type="dequeue"))
        step_nodes = []
        step_edges = []
        for n in G.neighbors(current):
            if visited[n] is False:
                q.insert(0, n)
                step_nodes.append(n)
                step_edges.append((current, n))
                visited[n] = True
                parent_mapping[n] = current

        steps.append(Step(step_nodes, step_edges, type="enqueue"))
    return dict(parent_mapping.items()), steps
