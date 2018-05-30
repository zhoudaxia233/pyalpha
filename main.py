from reader import read
from alpha import Alpha
import sys

def main(argv):
    log = read(argv[1])
    pn = Alpha(log)
    print(pn)

if __name__ == '__main__':
    main(sys.argv)
