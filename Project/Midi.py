import sys
import fileio

import Pmf
import Cdf
import Zipf

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
    pattern = fileio.read_midifile(fname)
    notes = []
    for track in pattern:
        for event in track:
            if event.name == "Note On":
                notes.append(event.data[0])
    pairs = []
    for i in range(len(notes)-1):
        pairs.append((notes[i], notes[i+1]))
    hist = Pmf.MakeHistFromList(pairs)
    Zipf.plot_ranks(hist, 'log')

if __name__ == '__main__':
    main(*sys.argv)
