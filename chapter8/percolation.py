import random



class Percolation(object):
    def __init__(self, n):
        self.arr = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(False)
            self.arr.append(tmp)

    def setPorous(self, i, j):
        self.arr[i][j] = True

    def unsetPorous(self, i, j):
        self.arr[i][j] = False

    def percolate(self):
        s = []
        visited = set()
        for i in range(len(self.arr)):
            if self.arr[i][0]:
                s.append((i,0))
            visited.add((i, 0))
        
        while len(s) > 0:
            i,j = s[len(s)-1]
            if j == len(self.arr) - 1:
                return True
            s.pop(len(s)-1)
            visited.add((i,j))
            for (a,b) in [(1,0), (0,1), (-1,0), (0,-1)]:
                ia, ib = (i+a, j+b)
                if ia >= 0 and ia < len(self.arr) and ib >= 0 and ib < len(self.arr):
                    if self.arr[ia][ib] and not((ia,ib) in visited):
                        s.append((ia,ib))
        return False


def porousSteps(n):
    perc = Percolation(n)
    for i in range(n*n):
        while True:
            ind = (random.randint(0, n-1), random.randint(0, n-1))
            if perc.arr[ind[0]][ind[1]]:
                continue
            perc.setPorous(*ind)
            break
        if perc.percolate():
            return i

def calcRp(n, tries):
    vals = []
    for i in range(tries):
        vals.append(porousSteps(n))
    # print vals
    return (reduce(lambda x, y: x + y, vals) / float(len(vals))) / float(n*n)




def main(script):
    print calcRp(50, 1000)
    print script


    

if __name__ == '__main__':
    import sys
    main(*sys.argv)
