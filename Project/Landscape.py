
import Life
import numpy
import scipy.ndimage

class RuleLife(Life.Life):
    """Implements Conway's Game of Life with an arbitrary rule set

    n:     the number of rows and columns
    """

    def __init__(self, n, rules = [3,12,13], mode='wrap', random=False):
        print rules
        super(RuleLife, self).__init__(n, mode, random)
        self.rules = rules

    def step(self):
        """Executes one time step."""
        con = scipy.ndimage.filters.convolve(self.array, self.weights,mode=self.mode)
        boolean = reduce(lambda state,elem: (con==elem)|state, self.rules, False)
        self.array = numpy.int8(boolean)


class HeightLife(RuleLife):
    def __init__(self, n, rules = [3,12,13], mode='wrap', random=False):

        super(HeightLife, self).__init__(n, rules, mode, random)
        self.heightmap = numpy.zeros((n, n), numpy.int32)


    def step(self):
        """Executes one time step."""
        con = scipy.ndimage.filters.convolve(self.array, self.weights,mode=self.mode)
        boolean = reduce(lambda state,elem: (con==elem)|state, self.rules, False)
        self.array = numpy.int8(boolean)
        for i in range(self.n):
            for j in range(self.n):
                if self.array[i][j] == 1:
                    self.heightmap[i][j] += 1


def main(script, *args):
    life = HeightLife(30, rules=[3, 12, 13], random=True)
    viewer = Life.LifeViewer(life)
    viewer.animate(steps=100)
    for i in range(life.n):
        print life.heightmap[i]
    print script, args


if __name__ == '__main__':
    import sys

    main(*sys.argv)
