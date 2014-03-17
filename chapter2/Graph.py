""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""


from sets import Set
from collections import deque

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        try:
            return self[v1][v2]
        except KeyError:
            return None

    def remove_edge(self, v, w):
        del self[v][w]
        del self[w][v]

    def vertices(self):
        return self.keys()

    def edges(self):
        s = Set([])
        for val in self.values():
            for v in val.values():
                s.add(v)
        return [v for v in s]

    def add_all_edges(self):
        for v in self.vertices():
            for w in self.vertices():
                if w != v:
                    self.add_edge(Edge(v,w))

    def out_verticies(self, v):
        return self[v].keys()

    def out_edges(self, v):
        return self[v].values()

    def is_connected(self):
        q = [self.keys()[0]]
        visited = Set(q)
        q = deque(q)
        while len(q) != 0:
            n = q.popleft()
            visited.add(n)
            for c in self[n].keys():
                if not c in visited:
                    q.append(c)
        return len(Set(self.keys()) - Set(visited)) == 0




def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    c = Vertex('c')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w,c], [e])
    print g
    print "..."
    print g.is_connected()


if __name__ == '__main__':
    import sys
    main(*sys.argv)
