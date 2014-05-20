import sys
import fileio

import Pmf
import Cdf
import Zipf


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def concatBits(b0, b1, bits = 8):
    ans = 0
    for i in range(bits):
        if (b1 & (1 << i)) != 0:
            ans = ans | (1 << i)
    for i in range(bits):
        if (b0 & (1 << i)) != 0:
            ans = ans | (1 << (i+8))
    return ans


class MidiError(Exception):
    """Base class for exceptions in this module."""
    pass

class Midi(object):
    def __init__(self, fname):
        self.bytes = []
        with open(fname, "rb") as f:
            while True:
                byte = f.read(1)
                if byte == "":
                    break
                self.bytes.append(ord(byte))
        self.check_header()
        self.file_format = self.bytes[9]
        self.tracks = concatBits(self.bytes[10],  self.bytes[11])
        self.delta = concatBits(self.bytes[12],  self.bytes[13])
        self.index = 14
        for i in range(self.tracks):
            self.read_track()
        if self.index != len(self.bytes):
            raise MidiError("Corrupt midi track: inconsistent length")
        


    def check_header(self):
        header = [77,84,104,100,0,0,0,6]
        for i in range(len(header)):
            if self.bytes[i] != header[i]:
                raise MidiError("Corrupt midi header")


    def read_track(self):
        header = [77,84,104,100]
        for i in range(len(header)):
            if self.bytes[i] != header[i]:
                raise MidiError("Corrupt track header")
        self.index += 4
        l = concatBits(self.bytes[self.index], self.bytes[self.index+1])
        r = concatBits(self.bytes[self.index+2], self.bytes[self.index+3])
        noBytes = concatBits(l, r, 16)
        self.index +=4
        self.index += noBytes


def linearEq(x, m, c):
    return m*x + c



def expEq(x, p, m, c):
    return m * np.power(x, -p) + c

def linearRegression(vals):
    x = np.array(vals)
    y = linearEq(x, 2.0, 1.0)
    yn = y + 0.001*np.random.normal(size=len(x))
    popt, pcov = curve_fit(linearEq, x, yn)
    print popt, pcov
    plt.figure()
    plt.plot(x, yn, 'ko', label="Original Noised Data")
    plt.plot(x, linearEq(x, *popt), 'r-', label="Fitted Curve")
    plt.legend()
    plt.show()



def expReg(xs, ys):
    x = np.array(xs)
    yn = np.array(ys)
    popt, pcov = curve_fit(expEq, x, yn)
    print popt, pcov
    plt.figure()
    plt.plot(x, yn, 'ko', label="Original Noised Data")
    plt.plot(x, expEq(x, *popt), 'r-', label="Fitted Curve")
    plt.legend()
    plt.show()


def plot(events):
    hist = Pmf.MakeHistFromList(events)
    Zipf.plot_ranks(hist, 'log')


def get_notes(fname):
    pattern = fileio.read_midifile(fname)
    notes = []
    for track in pattern:
        for event in track:
            if event.name == "Note On" and event.data[1] > 0:
                notes.append(event.data[0])
    return notes


def note_analysis(midipattern, n=2):
    notes = []
    for track in midipattern:
        for event in track:
            if event.name == "Note On" and event.data[1] > 0:
                notes.append(event)
    notes.sort(key=lambda x: x.tick)
    grouped = []
    for i in range(len(notes)-n+1):
        grouped.append(tuple([notes[i+j].data[0] for j in range(n)]))
    return grouped

def notevelocity_analysis(midipattern, n=1):
    notes = []
    for track in midipattern:
        for event in track:
            if event.name == "Note On" and event.data[1] > 0:
                notes.append(event)

    notes.sort(key=lambda x: x.tick)
    # print notes
    grouped = []
    for i in range(len(notes)-n+1):
        grouped.append(tuple([tuple(notes[i+j].data) for j in range(n)]))

    return grouped




def main(name, fname, *args):
    # print get_notes(fname)

    # m = Midi(fname)
    pattern = fileio.read_midifile(fname)
    events = note_analysis(pattern)
    plot(events)
    # ranks = Zipf.rank_freq(Pmf.MakeHistFromList(events))
    # xs = [float(i) for i, j in ranks]
    # ys = [float(j) for i, j in ranks]
    # expReg(xs, ys)
    # print ranks


if __name__ == '__main__':
    main(*sys.argv)
