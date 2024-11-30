"""
Aksa Vinod
30-11-2028
"""
def is_right_angle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2 + sides[1]**2:
        return True
    return False

side1=int(input("Enter the length of first side"))
side2=int(input("Enter the length of second side"))
side3=int(input("Enter the length of third side"))
if is_right_angle(side1,side2,side3):
    print("The given sides are the part of right angled triangle")
else:
    print("The given sides are not a part of right angled triangle")
