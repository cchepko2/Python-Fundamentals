import math

GRAVITY = 1.62 # Mun gravity

def main():
    angle = input("Enter an angle in degrees: ")
    angle = float(angle)
    angle = math.radians(angle)

    velocity = input("Enter a velocity in m/s: ")
    velocity = float(velocity)

    distance = velocity**2 * math.sin(2*angle)/GRAVITY
    
    print("The ball went", distance, "meters.", "Equals", distance*3.28, "feet." )

# If I am the main program, and not an import, run my main function
if( __name__ == "__main__"):
    main()