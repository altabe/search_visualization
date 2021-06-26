import tempfile
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
from IPython.display import Image, display, clear_output
import time


def display_graph(g):
    A = to_agraph(g)
    A.layout(prog='dot')
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        A.draw(f.name)
        display(Image(f.name))

class GraphAnimator():
    def __init__(self, plotting_interval_seconds=1) -> None:
        self._interval = plotting_interval_seconds
        self._last_display_time = time.time()

    def plot(self, G):
        time_since_last_display = time.time() - self._last_display_time
        time_to_sleep = self._interval - time_since_last_display
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)
        clear_output(wait=True)
        display_graph(G)
        self._last_display_time = time.time()
        