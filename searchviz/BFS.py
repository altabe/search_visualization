from copy import deepcopy
from collections import defaultdict
from searchviz.utils.color import color_edges, color_nodes
from searchviz.ipy_graph_display import Step


def BFS_search(G, start_node):
    steps = []
    parent_mapping = defaultdict(lambda: None)
    visited = defaultdict(lambda: False)
    visited[start_node] = True
    q = [start_node]
    steps.append(Step(nodes=[start_node], type="start"))
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


class BFSAnimator:
    def __init__(self, graph_animator):
        self.graph_animator = graph_animator

    def animate(self, G, steps):
        G = deepcopy(G)
        for step in steps:
            if len(step.nodes) + len(step.edges) == 0:
                continue
            if step.type == "start":
                color_nodes(G, step.nodes, "green")
            elif step.type == "enqueue":
                color_nodes(G, step.nodes, "red")
                color_edges(G, step.edges, "red")
            elif step.type == "dequeue":
                continue
            self.graph_animator.plot(G)
