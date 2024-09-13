def greet(student_name):
    student_name = "Susan"  # This name, as a function parameter, is a local varible to greet()
    print(f"Hello {student_name}!")

def main():
    print("Hello World!")

    name = "Corin"

    print(f"Hello {name}!")

    greet(name)

    print(f"Hello {name}!")

main()  # This is first unindected line and starts the main() function
        # which should be the beginning of the program.