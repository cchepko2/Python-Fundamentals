import sys

def tri_area(base, height):
    area = base*height/2
    return area

def unitTest():
    assert tri_area(3,4) == 6
    assert tri_area(0,0) == 0

    print("All test passed!", file=sys.stderr)

def main():
    unitTest()

    base, height = input("Enter a base and height for a triangle separated by spaces: ").split()
    base, height = map(float, (base, height)) #converts both strings,
    #base and height, into floating points numbers to be used for math

    #base = float(base)
    #height = float(height)

    area = tri_area(base, height)
    print(f"Area = {area}")

    if( area > 5.9 and base == 7.0):
        print("Above conditions satisifed...")

main()