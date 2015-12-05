import sys
import os 
import numpy as np 

if __name__ == '__main__':
    with open('puzzle_03_input.txt', 'r') as f:
        input_file = f.read()
    # initialize a blank grid 
    grid = np.zeros((4000, 4000))
    # set center to 0
    grid[2000,2000] = 1 
    x = 2000
    y = 2000
 
    for idx, char in enumerate(input_file):
        # update coordiates based on direction
        if char == 'v':
            y -= 1
        elif char == '^':
            y += 1
        elif char == '>':
            x += 1
        elif char == '<':
            x -= 1
        grid[x, y] = 1 
    print "Part 1:\n"
    print "Total number of unique houses:\t%s" % int((np.sum(np.sum(grid, axis=1))))

    man_grid = np.zeros((4000,4000))
    robo_grid = np.zeros((4000,4000))
    man_grid[2000,2000] = 1
    robo_grid[2000,2000] = 1
    my = 2000
    mx = 2000
    ry = 2000
    rx = 2000
    for idx, char in enumerate(input_file):
        if idx % 2 == 0:
            if char == 'v':
                my -= 1
            elif char == '^':
                my += 1
            elif char == '>':
                mx += 1
            elif char == '<':
                mx -= 1
            man_grid[mx, my] = 1 
        elif idx % 2 == 1:
            if char == 'v':
                ry -= 1
            elif char == '^':
                ry += 1
            elif char == '>':
                rx += 1
            elif char == '<':
                rx -= 1
            robo_grid[rx, ry] = 1
        else:
            print "opps"
    sum_grid = man_grid + robo_grid
    unraveled = np.ravel(sum_grid)
    unraveled[unraveled > 1] = 1 
    print "Part 2:\n"
    print "Total number from Robo and Manual santa:\t%s" % int(np.sum(unraveled))
