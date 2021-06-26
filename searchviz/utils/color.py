def color_nodes(G, nodes, color='red'):
    for n in nodes:
        G.nodes[n]['color'] = color
        G.nodes[n]['style']='filled'

def uncolor_node(G, n):
    G.nodes[n].pop('color', None)
    G.nodes[n].pop('style', None)

def color_edges(G, edges, color='red'):
    for e in edges:
        G.edges[e]['color']='red'

def uncolor_edge(G, e):
    G.edges[e].pop('color', None)
    
def uncolor_graph(G):
    for n in G.nodes:
        uncolor_node(G, n)
    for e in G.edges:
        uncolor_edge(G, e)