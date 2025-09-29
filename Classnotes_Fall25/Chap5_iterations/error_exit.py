def corin_input_digit():

    while(True):
        number = input("Enter a number: ")
        if(number.isdigit() == True):
            number = int(number)
        else:
            print("You are a wonderful person, but bad at input...")
            print("This has caused a critical error in this program...")
            print("Exiting...")
            return "Error"
    # Loop is done, got input
    return number