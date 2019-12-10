#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 9):
        print("{:d}{:d}".format(i, j + 1), end="")
        if (i != 8 or j + 1 != 9):
            print(", ", end="")
print("")
