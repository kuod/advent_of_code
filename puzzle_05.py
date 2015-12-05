import pdb
import numpy as np 


def vowel_check(line):
    vowel_count = []
    vowels = "aeiou"
    for v in vowels:
        vowel_count.append(line.lower().count(v))
    if sum(vowel_count) >= 3:
        return True
    else:
        return False

def double_letter(line):
    double_letter_ind = False
    for idx, char in enumerate(line):
        if idx == 0:
            last_char = char
        else:
            if char == last_char:
                double_letter_ind = True
                last_char = char
            else:
                last_char = char
    return double_letter_ind
    
def bad_string(line):
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    count = [] 
    for bs in bad_strings:
        count.append(line.lower().count(bs))
    if max(count) == 0:
        return True
    else:
        return False

def search_pairs(line):
    twomer = [line[j:][i:i+2] for j in [0,1] for i in range(0, len(line), 2)]
    twomer_mask = []
    for j in twomer:
        if len(j) == 1:
            next
        else:
            twomer_mask.append(j)
    if max([line.count(i) for i in twomer_mask]) != 1:
        return True
    else:
        return False

def search_repeats(line):
    threemer = [line[j:][i:i+3] for j in [0,1,2] for i in range(0, len(line), 3)]
    for val in threemer:
        if len(val) == 3:
            if val[0] == val[2]:
                return True
        else:
            next
    return False

if __name__ == '__main__':
    with open('puzzle_05_input.txt', 'r') as f:
        input_file = f.readlines()
    nice = 0
    naughty = 0
    for line in input_file:
        vowel_ind = vowel_check(line)
        double_let_ind = double_letter(line)
        bad_string_ind = bad_string(line)
        if vowel_ind and double_let_ind and bad_string_ind:
            nice += 1
        else:
            naughty += 1
    
    print "Part 1"
    print "Total number of nice:\t%s" % (nice)

    # New rules
    nice = 0 
    nice_cnt = 0
    test_strings = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

    for line in input_file:
        line = line.rstrip()
        pair_search_ind = search_pairs(line)
        search_repeat_ind = search_repeats(line)
        #if is_really_nice(line):
        #    nice_cnt += 1
        if pair_search_ind and search_repeat_ind:
            nice += 1
    print "Part 2"
    print "Total number of nice:\t%s" % (nice)
