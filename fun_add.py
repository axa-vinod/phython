"""
Aksa Vinod
3-12-2024
"""
def add_number(num1,num2):
    if num2==0:
        return num1
    else:
         return add_number(num1+1,num2-1)
print (add_number(6,4))