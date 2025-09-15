'''
Some examples of fruitless funtions: functions that do not return data to
the rest of the program.  Fruitless function can receive data.
'''

def greet():   # Fuitless function with no parameters
    print("Hello")
    print("World!")

def greet_name(name):   # Fuitless function a parameter
    name = "Corin"
    print(f"Hello {name}")
    print("World!")

def greet_name_and_return(name):   # Fuitless function a parameter
    name = "Corin"
    print(f"Hello {name}")
    print("World!")
    return name

def greet_name_list_reference(list_name):   # Fuitless function a parameter
    list_name[0] = "Corin"
    print(f"Hello {list_name}")
    print("World!")

greet()  # This is a call to the "greet()" function

main_name = "Xander"
greet_name(main_name)
print(main_name)

main_name = greet_name_and_return(main_name)
print(main_name)

main_name = ["Zelda", "Corin"]
greet_name_list_reference(main_name)
print(main_name)


