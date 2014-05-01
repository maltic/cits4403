import sys
import fileio

class Midi(object):
    def __init__(self, fname):
        self.bytes = []
        with open(fname, "rb") as f:
            while True:
                byte = f.read(1)
                if byte == "":
                    break
                self.bytes.append(ord(byte))




def main(name, fname, *args):
    #m = Midi(fname)
    print fileio.read_midifile(fname)


if __name__ == '__main__':
    main(*sys.argv)
