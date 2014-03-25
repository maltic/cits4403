from RandomGraph import RandomGraph
from Graph import *
import random
from sets import Set
import math

import matplotlib.pyplot as pyplot

def avg(seq):
    return 1.0 * sum(seq) / len(seq)


class SamllWorldGraph(RandomGraph):

    def cluster_coef(self):
        return avg([self.cluster(self.out_vertices(v)) for v in self.vertices()])

    def cluster(self, set):
        k = len(set)
        if k < 2: return 1.0
        possible = (k * (k-1.0))/2
        edges = [1 for v in set for w in set if v > w and self[v].get(w, False)]
        return len(edges) / possible

    def rewire(self, p=0.01):
        # consider the edges in random order (this is slightly different
        # from Watts and Strogatz
        es = list(self.edges())
        random.shuffle(es)
        vs = self.vertices()
        
        for e in es:
            # if this edge is chosen, remove it...
            if random.random() > p: continue
            v, w = e
            self.remove_edge(e)

            # then generate a new edge that connects v to another vertex
            while True:
                w = random.choice(vs)
                if v is not w and not self.has_edge(v, w): break

            self.add_edge(Edge(v, w))

    def avg_path_len(self):
        allp = self.floyd_warshall()
        return avg([x for k in allp.values() for x in k.values() if x != sys.maxint])


def plot_avg_path_len():
    

    acc = []
    for i in range(1, 101):
        g = SamllWorldGraph([Vertex(c) for c in range(64)])
        g.add_regular_edges(8)
        g.rewire(i / 100.0 )
        acc.append(g.avg_path_len())


    pyplot.plot([x / 100.0 for x in range(1, 101)], acc)
    scale = 'linear'
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('p')
    pyplot.ylabel('L(p)')
    pyplot.show() 


def plot_cluster_coef():
    

    acc = []
    for i in range(1, 101):
        g = SamllWorldGraph([Vertex(c) for c in range(128)])
        g.add_regular_edges(8)
        g.rewire(i / 100.0 )
        acc.append(g.cluster_coef())


    pyplot.plot([x / 100.0 for x in range(1, 101)], acc)
    scale = 'linear'
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('p')
    pyplot.ylabel('C(p)')
    pyplot.show()

def main(script, *args):
    plot_avg_path_len()
    plot_cluster_coef()
    g = SamllWorldGraph([Vertex(c) for c in range(128)])
    g.add_regular_edges(8)
    g.rewire(1)
    print g.avg_path_len()

if __name__ == '__main__':
    import sys
    main(*sys.argv)