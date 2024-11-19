"""
Aksa Vinod
19-11-2024
"""

num=int(input("Enter a number"))
for i in range(1,num+1):
    for i in range(i):
        print("*",end=" ")
    print()
print("SECOND PATTERN")
for i in range(num+1,0,-1):
        for i in range(i):
            print("*",end=" ")
        print()
print("THIRD PATTERN")
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()
print("FOURTH PATTERN")
for i in range (num,0,-1):
    for j in range(num-i):
        print(" ",end=" ")
    for k in range (2*i-1):
        print("*",end=" ")
    print()
