while(True):
    end = input("Print the end of the loop?")
    if(end.lower() != 'y'):
        print("More loops!")
        continue

    print("The end of the loop")
    break

# Repeat until user says no
while(True):
    print("Doing stuff...")
    
    if(input("Break?") == 'y'):
        break
else:
    print("Thanks for playing!")  # dead code because previous loop must break

while(True):
    end = input("Print the end of the loop?")
    if(end.lower() != 'y'):
        print("More loops!")
        continue

    print("The end of the loop")
    break

# Repeat until user says no or i reaches 3
i = 0
while(i <= 3):
    print(i, "Doing stuff...")
    i += 1
    
    if(input("Break?") == 'y'):
        break
else:
    print("Thanks for playing!")  # prints if previous loop finishs without break
    
