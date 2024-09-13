# This program prints "Susan" twice because name is used as a local
# varible in the greet() function

name = "Corin"  # not tabbed in - globabl variable accessable by any function
# GLOBAL VARIABLES CAN CAUSE CONFUSION! I DON"T LIKE THEM IN THIS CLASS

def greet():
    name = "Susan"    
    print(f"Hello {name}.")
    

greet()
greet()