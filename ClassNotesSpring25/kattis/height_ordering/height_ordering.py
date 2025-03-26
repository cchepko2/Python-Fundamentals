'''
Corin Chepko
03/24/25
Kattis Problem - https://open.kattis.com/problems/height
Algorithm Steps:
    Collect input:
        input number of test cases
        for each test case:
            input test number and 20 numbers for heights
'''

def steps_back(heights):
    total_steps_taken = 0

    # outter loop goes through each height starting from index 1
        #inner loop goes through all previous indexs to see if someone is shorter
    
    return total_steps_taken


import sys

print("Enter number of test cases: ", file=sys.stderr)
number_tests = int(input())

inputs = []

for i in range(1, number_tests+1): # Starting from count of one, collect number_test sets of numbers
    line_nums = input().split() # Collect line of numbers and split into list
    line_nums = line_nums[1::]  # slice off first number, we don't need it
    line_nums = list(map(int, line_nums))
    inputs.append(line_nums)
    # Handy function to convert list to number of steps taken back goes here

print(inputs)