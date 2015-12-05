import sys
import os 


if __name__ == '__main__':
    with open('puzzle_01_input.txt', 'r') as f:
        input_file = f.read()
    up = input_file.count('(')
    down = input_file.count(')')
    print "Part 1:\t\tNet floors traveled:\t%s" % (up - down)
    floor = 0
    for idx, char in enumerate(input_file):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print "Part 2:\t\tPosition when entering basement:\t%s" % (idx + 1)
