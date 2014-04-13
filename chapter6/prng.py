import time


class LinearCongruentialGenerator(object):
    def __init__(self, seed = 1, a = 48271, c = 0, m = 2147483647):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed


def main():
    prng = LinearCongruentialGenerator(int(round(time.time() * 1000)))
    for i in range(1000):
        print prng.next()

if __name__ == "__main__":
    main()