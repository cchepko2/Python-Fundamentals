def main():
    grade = float(input("Enter your numerical grade: "))
    letter = check_grade(grade)
    print(f"You got a {letter}")

    letter = better_check_grade(grade)
    print(f"You got a {letter}")

# Written in wrong order
def check_grade(grade):
    if grade < 60:
        letter = 'F'
    elif grade > 60:
        letter = 'D'
    elif grade > 70:
        letter = 'C'
    elif grade > 80:
        letter = 'B'
    else:
        letter = 'A'
    
    return letter

def better_check_grade(grade):
    if grade < 60:
        letter = 'F'
    elif grade < 70:
        letter = 'D'
    elif grade < 80:
        letter = 'C'
    elif grade < 90:
        letter = 'B'
    else:
        letter = 'A'
    
    return letter

main()