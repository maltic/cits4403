
class Link(object):
    def __init__(self, c, n):
        self.contents = c
        self.next = n

class FIFO(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, i):
        if self.head == None:
            self.head = Link(i, None)
            self.tail = self.head
        else:
            self.tail.next = Link(i, None)
            self.tail = self.tail.next

    def pop(self):
        if self.head == None:
            return None
        else:
            i = self.head.contents
            self.head = self.head.next
            return i


def main(script, *args):
    q = FIFO()
    q.push(4)
    q.push(10)
    print q.pop()
    print q.pop()
    q.push(9)
    print q.pop()


if __name__ == '__main__':
    import sys
    main(*sys.argv)