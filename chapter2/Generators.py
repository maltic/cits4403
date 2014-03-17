import string
from itertools import count
def alphabet_cycle():
	while True:
		for d in count():
			for c in string.lowercase:
				yield c+str(d)

def main():
    for l in alphabet_cycle():
    	print l


if __name__ == '__main__':
    main()