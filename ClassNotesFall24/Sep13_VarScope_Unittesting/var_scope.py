name = "Corin"  # not tabbed in - globabl variable accessable by any function
# GLOBAL VARIABLES CAN CAUSE CONFUSION! I DON"T LIKE THEM IN THIS CLASS

# This program prints "Corin" and then "Susan" because name is used as a global
# varible in the greet() function

def greet():
    global name
    
    print(f"Hello {name}.")
    name = "Susan"
    

greet()
greet()
