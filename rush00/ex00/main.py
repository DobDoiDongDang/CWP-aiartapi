import sys
from checkmate import checkmate
def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            with open(sys.argv[i], 'r') as f:
                checkmate(f.read())
    else:
        board = """\
                ......R.
                ........
                R.......
                ........
                ........
                ........
                ...K....
                ........\
                """
        checkmate(board)

if __name__ == "__main__":
    main()
