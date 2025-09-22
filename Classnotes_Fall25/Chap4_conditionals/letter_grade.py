print("Enter a grade from 0 to 100")

grade = float(input())
if(grade > 60):   # This logic is backwards
    letter = 'D'
elif(grade > 70):
    letter = 'C'
elif(grade > 80):
    letter = 'B'
else:
    letter = 'A'

print(f"A grade of {grade} is a {letter}.")

# This if and else set works
print("Enter a grade from 0 to 100")
grade = float(input())
if(grade >= 90):   # This logic is correct
    letter = 'A'
elif(grade >= 80):
    letter = 'B'
elif(grade >= 70):
    letter = 'C'
elif(grade >= 60):
    letter = 'D'
else:
    letter = 'F'

print(f"A grade of {grade} is a {letter}.")