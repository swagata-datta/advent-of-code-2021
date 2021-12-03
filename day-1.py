'''Advent of Code 2021

Day 1:'''

from toolkit import *

input = inputfile('input_files\day_1.txt')

testcase = '''199
200
208
210
200
207
240
269
260
263'''

testcase = [int(i) for i in testcase.split()]

def larger_than_prev_count(input_):
    """Takes in input file which is a list of numbers
    Returns the number of occurences of a measurement being larger than the previous measurement"""
    sum = 0
    for i in range(1, len(input_)):
        if input_[i] > input_[i-1]:
            sum += 1
    return sum

assert larger_than_prev_count(testcase) == 7

input = [int(i) for i in input]

print(larger_than_prev_count(input))


