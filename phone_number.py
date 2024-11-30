"""
Aksa Vinod
30-11-2024
"""

def check_number():
    number=input("Enter your phone number")
    length=len(number)
    if length==10:
         if number[0]=='7'or number[0]=='8' or number[0]=='9':
             print("Valid number ")
         else:
             print("Invalid number")
check_number()
