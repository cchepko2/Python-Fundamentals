import math
import sys

GRAVITY = 1.62 # Mun gravity

def main():
    angle = input("Enter an angle in degrees: ")
    angle = float(angle)
    angle = math.radians(angle)

    velocity = input("Enter a velocity in m/s: ")
    velocity = float(velocity)

    distance = projectile_calc(angle, velocity)
    
    print("The ball went", distance, "meters.", "Equals", distance*3.28, "feet." )


#def projectile_calc(angle: float, velocity: float) -> float:
def projectile_calc(angle, velocity):
    distance = velocity**2 * math.sin(2*angle)/GRAVITY
    return distance

def test():
    error = 10e-6
    assert(projectile_calc(0,0) == 0)
    print(projectile_calc(math.radians(90),100))
    assert(math.fabs(projectile_calc(math.radians(90),100)-0.0) <= error)
    print("All test passed!", file=sys.stderr)


# If I am the main program, and not an import, run my main function
if( __name__ == "__main__"):
    test()
    main()