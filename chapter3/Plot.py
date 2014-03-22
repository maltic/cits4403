import matplotlib.pyplot as pyplot

def graph():
	pyplot.plot(range(100), [x*2 for x in range(100)])
	scale = 'log'
	pyplot.xscale(scale)
	pyplot.yscale(scale)
	pyplot.title('')
	pyplot.xlabel('n')
	pyplot.ylabel('run time (s)')
	pyplot.show()


def main(script, *args):
    graph()


if __name__ == '__main__':
    import sys
    main(*sys.argv)