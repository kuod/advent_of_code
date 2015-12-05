import numpy as np 


def calc_sq_ft(line):
    # integers of dimensions
    length, width, height = map(int, line.split('x'))
    # slack is the sq feet of smallest side
    slack = np.prod(np.sort((length, width, height))[:-1])
    sq_feet = (2*length*width) + (2*width*height) + (2*length*height)
    sq_feet += slack
    return sq_feet

def calc_ribbon(line):
    # perimeter of shortest side
    # volume of box
    length, width, height = map(int, line.split('x'))
    bow = np.prod((length, width, height))
    perimeter = np.sum(np.sort((length, width, height))[:-1]) * 2 
    bow_length = perimeter + bow 
    return bow_length 

if __name__ == '__main__':
    with open('puzzle_02_input.txt', 'r') as f:
        input_file = f.readlines()
    sq_feet_arr = []
    ribbon_arr = []
    for line in input_file:
        sq_feet_arr.append(calc_sq_ft(line))
        ribbon_arr.append(calc_ribbon(line))
    print "Part 1:\n"
    print "Total square feet:\t%s" % (np.sum(sq_feet_arr))
    print "Part 2:\n"
    print "Total ribbon length:\t%s" % (np.sum(ribbon_arr))
