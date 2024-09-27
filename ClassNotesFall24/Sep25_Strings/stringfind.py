"""
String Find, Len, Slicing Exercises
Updated By: Seth Kaufman
CSCI 110 Lecture
Date: 25 SEP 2024

This file works through a few examples of slicing strings and methods you can use.

"""
# Please return the string pizza
lunch = "I ate pizza for lunch."

########
# Counting the characters in the list manual method
########
subStringTest = lunch[6:11]
print(subStringTest)

########
# Using find() and len() to pick pizza out of string
########
lunch = "I ate pizza for lunch."
targetString = "pizza"

# using find() to get the start of string
beg = lunch.find(targetString)
print(beg)

# length of string to slice
lenStr = len(targetString)
print(lenStr)


# length of string to slice
dinner = "I ate pizza for lunch and pizza for dinner."
endIdx = dinner.rfind(targetString)
print('rfind',endIdx)

# end of range for slicing
end = beg + lenStr

# print sliced string
print(lunch[beg:end])