"""
Name Aksa Vinod
Date 22-10-2024
Version1.1
"""
tem=int(input("Enter temperature :"))
cel=input("If this in (C)elsius or (F)ahrenheit ?")
if cel=="C":
    F=(9/5*tem)+32
    print(tem,"celsius is ",F,"Fahrenheit")
else :
    C=5/9*(tem-32)
    print(tem,"Fahrenheit is",C,"celsius")