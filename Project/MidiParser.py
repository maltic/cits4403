import sys

class Midi(object):
    def __init__(self, fname):
        self.bytes = []
        with open(fname, "rb") as f:
            byte = f.read(1)
            while byte != "":
                byte = f.read(1)
                self.bytes.append(byte)




def main(name, fname, *args):
    m = Midi(fname)
    print m.bytes


if __name__ == '__main__':
    main(*sys.argv)
