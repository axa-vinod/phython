"""
Aksa Vinod
3-12-2024
"""
def multiply_number(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply_number(n1,n2-1)
print(multiply_number(4,5))