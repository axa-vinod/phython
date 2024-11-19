"""
Aksa Vinod
19-11-2024
Version1.1
"""

list1=[]
list2=[]
list1_size=int(input("Enter your number of elements in list 1"))
print(f"Enter the elements of list1:")
for i in range (list1_size):
    list1.append(int(input()))
list2_size=int(input("Enter your number of elements in list 2"))
print(f"enter the elements of list2:")
for i in range(list2_size):
    list2.append(int(input()))
combined_list=list1+list2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()
merge_list=even_list+odd_list
print(merge_list)