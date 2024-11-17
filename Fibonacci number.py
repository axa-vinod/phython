limit=int(input("Enter your limit"))
first_number=1
second_number=0
third_number=0
while(third_number<limit):
    print(third_number,end=" ")
    third_number=first_number+second_number
    first_number=second_number
    second_number=third_number