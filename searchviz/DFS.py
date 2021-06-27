from copy import deepcopy
from collections import defaultdict
from searchviz.utils.color import color_edges, color_nodes
from searchviz.ipy_graph_display import Step


def DFS_search(G, start_node):
    steps = []
    parent_mapping = defaultdict(lambda: None)
    visited = defaultdict(lambda: False)
    visited[start_node] = True
    q = []
    for e in G.out_edges(start_node):
        q.append(e)
        visited[e[1]] = True
    steps.append(Step(nodes=[start_node], type="start"))
    while len(q) > 0:
        current_edge = q.pop()
        current_node = current_edge[1]
        steps.append(Step(nodes=[current_node], edges=[current_edge], type="pop"))
        step_nodes = []
        step_edges = []
        for n in G.neighbors(current_node):
            if not visited[n]:
                q.append((current_node, n))
                step_nodes.append(n)
                step_edges.append((current_node, n))
                visited[n] = True
                parent_mapping[n] = current_node

        steps.append(Step(step_nodes, step_edges, type="push"))
    return dict(parent_mapping.items()), steps


class DFSAnimator:
    def __init__(self, graph_animator):
        self.graph_animator = graph_animator

    def animate(self, G, steps):
        G = deepcopy(G)
        for step in steps:
            if len(step.nodes) + len(step.edges) == 0:
                continue
            if step.type == "start":
                color_nodes(G, step.nodes, "green")
            elif step.type == "push":
                continue
            elif step.type == "pop":
                color_edges(G, step.edges, "red")
                color_nodes(G, step.nodes, "red")
            self.graph_animator.plot(G)
