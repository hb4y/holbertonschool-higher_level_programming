#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("0 arguments.")
        exit()
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

    for index, data in enumerate(sys.argv[1:]):
        print("{:d}: {}".format(index + 1, data))
