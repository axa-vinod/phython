"""
Aksa Vinod
19-11-2024
Version1.1
"""
my_list=[15,10,20,10,25,30]
unique_list=[]
for num in my_list:
    if num not in unique_list:
        unique_list.append(num)
print(f"Original list  is {my_list}")
print(unique_list)

