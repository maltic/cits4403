import random

class Segregrate(object):
    def __init__(self, n, ppl, cutoff):
        self.locs = {}
        self.n = n
        self.ppl = ppl
        self.cutoff = cutoff
        for i in range(ppl):
            self.locs[self.unoccupied()] = random.choice([1, 2])

    def validCell(self, r, c):
        if r < 0: return False
        if c < 0: return False
        if r >= self.n: return False
        if c >= self.n: return False
        if not((r,c) in self.locs): return False
        return True

    def unoccupied(self):
        while True:
            rr = random.randint(0, self.n-1)
            rc = random.randint(0, self.n-1)
            if not ((rr,rc) in self.locs):
                return (rr,rc)

    def display(self):
        l = [[0 for i in range(self.n)] for i in range(self.n)]
        for (r,c) in self.locs.keys():
            l[r][c] = self.locs[(r,c)]
        for ll in l:
            print ll


    def simulationStep(self):
        for (r, c) in self.locs.keys():
            offsets = [(1,0), (0,1), (-1,0), (0,-1)]
            niggs = 0
            for (ro, co) in offsets:
                rr = r + ro
                cc = c + co
                if self.validCell(rr, cc) and self.locs[(rr,cc)] != self.locs[(r,c)]:
                    niggs += 1
            if niggs > self.cutoff:
                l = self.unoccupied()
                self.locs[l] = self.locs[(r,c)]
                del self.locs[(r,c)]





def main(name, n = 20, ppl = 380, *args):
    seg = Segregrate(int(n), int(ppl), 2)
    for i in range(100):
        seg.simulationStep()
    seg.display()


if __name__ == '__main__':
    import sys
    main(*sys.argv)
