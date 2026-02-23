'''
Corin Chepko
2/23/26
Program: Distance of golf ball hit on the Moon
Algorithm:
    input angle in degrees
    convert angle to float and to radians
    input velocity
    convert to float

    Calculate distance

    print(distance with description)

    Test Function:
        assert a couple test cases
'''

import math
import Mun_art
import sys

GRAVITY = 1.62

def main():
    print(Mun_art.art1)

    angle = input("Enter an angle in degrees: ")
    angle = float(angle)
    angle = math.radians(angle)

    velocity = input("Enter a velocity in m/s: ")
    velocity = float(velocity)

    distance = calc_distance(angle, velocity)

    print("The distance traveled is", distance, "meters.")


#def calc_distance(angle, velocity):
def calc_distance(angle: float, velocity: float) -> float:
    '''
    Returns distance (float) using V**2 * sin(2*angle)/Gravity
    Inputs angle (radians) and velocity (m/s)
    '''

    distance = velocity**2 * math.sin(2*angle)/GRAVITY
    return distance

def test():
    error = 10e-6
    expected = 0.0
    assert(math.fabs(calc_distance(0, 0)-expected) < error)
    assert(math.fabs(calc_distance(math.pi/2, 1000)-expected) < error)
    expected = 5.278088631568961
    assert(math.fabs(calc_distance(math.radians(10), 5) - expected) < error)
    print("All tests passed!", file=sys.stderr)


if __name__ == "__main__":
    test()
    main()