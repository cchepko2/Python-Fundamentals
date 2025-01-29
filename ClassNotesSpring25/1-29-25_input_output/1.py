'''Strings and escape sequences'''

a_string = "Hello beautiful world!"

# I want to use "'s in my string, so I enclose the string with 
# single ''s
b_string = 'Hello "beautiful" world!'

# I want to use both single and double quotes, so I use triple quotes
# to enclode my string
c_string = '''Hello ' "beautiful" ' world '''

# Using escape characters to put in triple quotes
d_string = '''Hello \'\'\' ' "beautiful" ' \'\'\' world '''

# Using escape characters to put in triple quotes and add backslashes
e_string = '''\\Hello \'\'\' ' "beautiful" ' \'\'\' world\\'''

raw_string = R'''\\Hello \'\'\' ' "beautiful" ' \'\'\' world\\'''

print(a_string)
print(b_string)
print(c_string)
print(d_string)
print(e_string)
print(raw_string)

# Let's try some escape sequeces!
print("Hello\n\tI'm printing things weird\nthis line will be\rbonkered!")