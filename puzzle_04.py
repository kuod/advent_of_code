import sys
import os 
import numpy as np 
import hashlib

if __name__ == '__main__':
    input_string = 'yzbqklnj'
    done_bool = True
    n_val = 0
    while done_bool:
        test_string = input_string + str(n_val)
        if n_val % 1000000 == 0:
            print n_val
        if hashlib.md5(test_string).hexdigest()[0:6] == '000000':
            done_bool = False
            print n_val
        else:
            n_val += 1 
