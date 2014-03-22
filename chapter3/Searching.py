
def bisect(elems, key):
    l = 0
    r = len(elems)-1
    while l <= r:
        mid = (r+l)/2
        if elems[mid] == key:
            return mid
        elif elems[mid] > key:
            r = mid-1
        else:
            l = mid+1
    return None

def main():
    print bisect([i for i in range(50)], 49)


if __name__ == '__main__':
    main()
