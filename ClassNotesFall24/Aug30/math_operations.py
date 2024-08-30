'''
Author: Corin Chepko
Date: 8/30/24
Program: Ascii Art
Algorithm:
    Ask for user name
    Collect user name
    Greet User
    Use varibles to define 4 pieces of ascii art
    print(art)

    Cite online sources for ascii art if used
'''

minutes = int( input("Please enter number of minutes to convert: ") )

hours = minutes // 60
rem_minutes = minutes % 60

print(str(hours) + " hours, and", str(rem_minutes) + " minutes.")
print(str(hours) + " hours, and " + str(rem_minutes) + " minutes.")

answer_string = str(hours) + " hours, and " + str(rem_minutes) + " minutes."
print(answer_string)