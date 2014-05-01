""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import numpy
import scipy.ndimage

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot





class Life(object):
    """Implements Conway's Game of Life.

    n:     the number of rows and columns
    """

    def __init__(self, n, mode='wrap', random=False):
        """Attributes:
        n:      number of rows and columns
        mode:   how border conditions are handled
        array:  the numpy array that contains the data.
        weights: the kernel used for convolution
        """
        self.n = n
        self.mode = mode
        if random:
            self.array = numpy.random.random_integers(0, 1, (n, n))
        else:
            self.array = numpy.zeros((n, n), numpy.int8)

        self.weights = numpy.array([[1,1,1],
                                    [1,10,1],
                                    [1,1,1]])

    def add_glider(self, x=0, y=0):
        coords = [(0,1), (1,2), (2,0), (2,1), (2,2)]
        for i, j in coords:
            self.array[x+i, y+j] = 1

    def loop(self, steps=1):
        """Executes the given number of time steps."""
        [self.step() for i in xrange(steps)]

    def step(self):
        """Executes one time step."""
        con = scipy.ndimage.filters.convolve(self.array, 
                                             self.weights,
                                             mode=self.mode)
        boolean = (con==3) | (con==12) | (con==13)
        self.array = numpy.int8(boolean)

    def load_from_life_file(self, fname):
        """ Parses and loads life 1.06 file """
        self.array = numpy.zeros((n, n), numpy.int8)
        f = open(fname, 'r')
        header = f.readline()
        for line in f:
            nums = line.split(" ")
            x, y = int(nums[0]), int(nums[1])
            self.array[(x + self.n) % self.n, (y + self.n) % self.n] = 1

class Turmite(object):
    def __init__(self, x, y, direc = 0):
        self.x = x
        self.y = y
        self.dir = direc

    def step(self, arr, wrap):
        cellIsWhite = arr[self.x, self.y]

        if cellIsWhite:
            arr[self.x, self.y] = 0
        else:
            arr[self.x, self.y] = 1

        self.dir = ((self.dir-1) if cellIsWhite == 1 else (self.dir+1)) % 4
        
        if self.dir == 0:
            self.y = (self.y - 1) % wrap
        elif self.dir == 1:
            self.x = (self.x+1) % wrap
        elif self.dir == 2:
            self.y = (self.y+1) % wrap
        else:
            self.x = (self.x-1) % wrap

class TurmiteLife(Life):
    def __init__(self, n, mode='wrap', random=False):
         super(TurmiteLife, self).__init__(n, mode, random)
         self.turmites = []


    def step(self):
        for turm in self.turmites:
            turm.step(self.array, self.n)

    def add_trumite(self, turm):
        self.turmites.append(turm)




class LifeViewer(object):
    """Generates an animated view of the grid."""
    def __init__(self, life, cmap=matplotlib.cm.gray_r):
        self.life = life
        self.cmap = cmap

        self.fig = pyplot.figure()
        pyplot.axis([0, life.n, 0, life.n])
        pyplot.xticks([])
        pyplot.yticks([])

        self.pcolor = None
        self.update()

    def update(self):
        """Updates the display with the state of the grid."""
        if self.pcolor:
            self.pcolor.remove()

        a = self.life.array
        self.pcolor = pyplot.pcolor(a, cmap=self.cmap)
        self.fig.canvas.draw()

    def animate(self, steps=10):
        """Creates the GUI and then invokes animate_callback.

        Generates an animation with the given number of steps.
        """
        self.steps = steps
        self.fig.canvas.manager.window.after(1000, self.animate_callback)
        pyplot.show()

    def animate_callback(self):
        """Runs the animation."""
        for i in range(self.steps):
            self.life.step()
            self.update()


def main(script, n=20, *args):

    n = int(n)

    life = TurmiteLife(n, random=False)
    life.add_trumite(Turmite(7, 4))
    #life.add_trumite(Turmite(7, 5))
    #life.add_glider()
    viewer = LifeViewer(life)
    viewer.animate(steps=300)


if __name__ == '__main__':
    import sys

    profile = False
    if profile:
        import cProfile
        cProfile.run('main(*sys.argv)')
    else:
        main(*sys.argv)
