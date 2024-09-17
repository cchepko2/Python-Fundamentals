def main():
    num = int(input("Enter in a number"))


    if(num > 0):
        if(num % 2 == 0):
            print("num is positive and even")
        else:
            print("num is positive and odd")
    else:
        if(num % 2 == 0):
            print("num is negative and even")
        else:
            print("num is negative and odd")

    # Alternatively we can use 4 conditionals with multiple conditions 
    if(num > 0 and num%2):
        print("num is positive and even")
    '''And so on...'''

    message = ""
    if( num > 0):
        message = message + "!!!The number is positive and "
    else:
        message = message + "!!!The number is negative and "
    
    if( num %2 == 0):
        message += "even."
    else:
        message += "odd"
    
    print(message)
    


main()