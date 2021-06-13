import tempfile
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
from IPython.display import Image, display


def display_graph(g):
    A = to_agraph(g)
    A.layout(prog='dot')
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        A.draw(f.name)
        display(Image(f.name))