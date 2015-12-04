import sys
import os 


if __name__ == '__main__':
    with open('puzzle_01_input.txt', 'r') as f:
        input_file = f.read()
    up = input_file.count('(')
    down = input_file.count(')')
    print up 
    print down
    print up - down
