a=1
b=1

if a==1:
    print("It's True!")

if a==1 and b==1:
    print("Both a and b are True.")

if a==1 or b==1:
    print("Either a or b is True.")

again = input("Do you want to play again? (Y/N): ")

# This is always True, because the or conditionals are not conditonal statements
if again=='Y' or 'y' or 'yes' or 'yeah' or 'Yes':
    print("Always True!")

# Do this instead, full conditionals for each or
if again=='Y' or again=='y' or again=='yes' or again=='yeah' or again=='Yes':
    print("Let's play again")

# Pretend the next line is a test if a file is open
fileopen = True

if fileopen != True:
    print("A file error occured. Exiting...")
    exit()

# Here the file is open, I continue with code, the main code will not be indented
number = 1_00_0_00
number = 1e10
print(number)

