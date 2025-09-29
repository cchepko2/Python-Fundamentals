while(True):
    print("An infinite loop!")

    # Ask the user to play again, break if not
    again = input("Play again?")
    if(again[0].lower() == 'y'): # take the first character, 
                            # make it lower case, 
                            # and compare to 'y' for yes
        continue # go back to the beginning of the loop
    else:
        print("Thanks for playing!")
        break # I'm done, exit the loop