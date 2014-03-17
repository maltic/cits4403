import random
import Graph

class RandomGraph(Graph.Graph):


    def add_random_edges(self, r):
       for v in self.vertices():
            for w in self.vertices():
                if v < w and random.uniform(0,1) <= r:
                   self.add_edge(Graph.Edge(v,w))

def main(script, *args):
    v = Graph.Vertex('v')
    print v
    w = Graph.Vertex('w')
    print w
    e = Graph.Edge(v, w)
    print e
    g = RandomGraph([v,w], [e])
    g.add_random_edges(0.8)
    print g
    print "..."
    print g.out_edges(v)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
