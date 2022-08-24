#calculate the volume of a right circular cone

#input:
#consists of 2 lines of text
#first line contains integer r, the radius of the cone
#second line contains integer h, the height of the cone
#both r and h are between 1 and 100
#output:
#the volume of the right circular cone with radius and height. 
#the formula to calculate the volume is (pi * r^2 * h)/3

import math

PI = 3.141592653589793

def calculate_cone_volume():
    r = float(input("choose the radius of the cone: "))
    h = float(input("choose the height of the cone: "))
    value_cone = (PI * (r*r)  * h)/3
    return round(value_cone, 3)

#print(calculate_cone_volume(4, 6))
print(calculate_cone_volume())
