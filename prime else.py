"""
AKsa Vinod
Date 12-11-2024
version1.1
"""
N=int(input("Enter a number"))
for i in range(2,N):
      if N%i==0:
          print("The given number",N," is not prime number")
          break
else:
    print("The given number",N," is prime number")
