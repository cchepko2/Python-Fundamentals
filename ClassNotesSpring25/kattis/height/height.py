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

from typing import List
import sys
import os
#from pathlib import Path
#script_directory_pathlib = Path(__file__).parent.resolve()

def steps_back(heights: List):
    total_steps_taken = 0

    # outter loop goes through each height starting from index 1
    for current_student in range(1,len(heights)):
        #inner loop goes through all previous indexs to see if someone is shorter
        for students_in_front in range(0,current_student):
            if( heights[current_student] < heights[students_in_front] ):
                total_steps_taken += current_student - students_in_front
                current_height = heights[current_student]
                heights.remove(current_height)
                heights.insert(students_in_front, current_height) 
                break
    
    return total_steps_taken

def main():
    print("Enter number of test cases: ", file=sys.stderr)

    number_tests = int(input())

    inputs = []
 #   out_file = open(f"{script_directory_pathlib}/out.txt", 'w')

    for i in range(1, number_tests+1): # Starting from count of one, collect number_test sets of numbers
        line_nums = input().split() # Collect line of numbers and split into list
        line_nums = line_nums[1::]  # slice off first number, we don't need it
        line_nums = list(map(int, line_nums))
        # Handy function to convert list to number of steps taken back goes here
        steps = steps_back(line_nums)
        ans = f"{i} {steps}\n"
        print(ans, end="")
  #      out_file.write(ans)
    
#    out_file.close()

def test():
    heights = [4,3,2,1]
    assert( steps_back(heights) == 6)
    print("All tests passed!", file=sys.stderr)

if __name__ == "__main__":
    test()
    main()