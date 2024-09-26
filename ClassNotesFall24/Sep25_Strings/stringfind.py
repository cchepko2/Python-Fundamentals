
# Please return the string pizza

stringTest = "I ate pizza for lunch."

# Counting the characters in the list
subStringTest = stringTest[6:11]
# print(subStringTest)

# Using find and len to pick pizza out of string
targetString = "pizza"
beg = stringTest.find(targetString)

print(beg)

lenStr = len(targetString)

print(lenStr)

end = beg + lenStr

print(stringTest[beg:end])