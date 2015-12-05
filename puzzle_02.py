import numpy as np 


def calc_sq_ft(line):
    # integers of dimensions
    length, width, height = map(int, line.split('x'))
    # slack is the sq feet of smallest side
    slack = np.prod(np.sort((length, width, height))[:-1])
    sq_feet = (2*length*width) + (2*width*height) + (2*length*height)
    sq_feet += slack
    return sq_feet

if __name__ == '__main__':
    with open('puzzle_02_input.txt', 'r') as f:
        input_file = f.readlines()
    sq_feet_arr = []
    for line in input_file:
        sq_feet_arr.append(calc_sq_ft(line))
    print "Total square feet:\t%s" % (np.sum(sq_feet_arr))
