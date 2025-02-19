print("Enter a grade value and I'll print the letter grade: ")

grade = float(input())

if( grade >= 90):
    letter = 'A'
elif( grade >= 80):
    letter = 'B'
elif( grade >= 70):
    letter = 'C'
elif( grade >= 60):
    letter = 'D'
else:
    letter = 'F'

print(f"Letter grade for a score of {grade} = {letter}")