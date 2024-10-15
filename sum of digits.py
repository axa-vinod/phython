"""
Name Aksa Vinod
Date15-10-2024
Version1.1
python programme to determine the sum of digits
"""
num=int(input("enter a number"))
sum=0
while (num>0):
    remainder=num%10
    num=num//10
    sum+=remainder
print(sum)