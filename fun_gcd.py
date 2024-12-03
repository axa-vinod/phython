"""
Aksa Vinod
3-12-2024
"""
def gcd(n1,n2):
    if n1%n2==0:
        return n1
    else:
        return gcd(n2, n1%n2)
print(gcd(1022,516))