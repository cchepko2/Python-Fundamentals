'''
A program that is an extension the the Kattis problem - "The Last Problem"

Algorithm Steps:
    1. input a name
    2. print "Hello and goodbye {name}"

    repeat 1 and 2 3 times
'''

'''
name = input()
print(f"Hello and goodbye {name}")

name = input()
print(f"Hello and goodbye {name}")

name = input()
print(f"Hello and goodbye {name}")
'''

# Using a function:
def hello_and_goodbye():  # This function does not need any data, 
                        # and is not returning any data to the rest of the program
                        # ie: a fruitless function
    name = input()
    print(f"Hello and Goodbye {name}")

hello_and_goodbye()
hello_and_goodbye()
hello_and_goodbye()