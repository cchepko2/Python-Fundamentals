while(True):
    print("Enter 3 numbers separated by a space: ")

    try:
        sidaA, sideB, sideC = input().split()
    except ValueError:
        print("Invalid input!")
        continue

    break

print(sidaA, sideB, sideC)