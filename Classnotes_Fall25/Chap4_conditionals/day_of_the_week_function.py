def day_of_week(day: int):
    if( day == 0 ):
        print("It's Monday")
    elif( day == 1 ):
        print("It's Tuesday")
    elif( day == 2 ):
        print("It's Wednesday")
    elif( day == 3 ):
        print("It's Thursday")
    elif( day == 4 ):
        print("It's Friday")
    elif( day == 5 ):
        print("It's Saturday")
    else:
        print("It's Sunday")



day_of_week_integer = int(input("Enter an interger for the day of the week: "))
day_of_week(day_of_week_integer)

