import math

#Get the Variables
distance =  round(float(input("Enter hours travelled: ")) * float(input("Enter meters per second: ")) * 3.6, 3)
degrees = -(int(input("Enter the degrees: ")) - 90)

#degree logic
if degrees <  -180:
    degrees = 360 + degrees
    
#solution variables
x = distance * float(math.cos(math.radians(degrees)))
y = distance * float(math.sin(math.radians(degrees)))

#final answer:
if x < 0:
    print(f"The surface will occur {-x: .3f} km west ", end="")
else:
    print(f"The surface will occur {x: .3f} km east ", end="")
if y < 0:
    print(f"and {-y: .3f} km south.")
else:
    print(f"and {y: .3f} km north.")
