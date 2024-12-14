"""
Aksa Vinod
13-12-2024
"""
import random
from types import new_class

print("Let's start the game ")
print("You have the choice of choosing 3 doors and inside one door there is a car ")
print("Choose wisely and Good Luck")
participant_choice=int(input("Enter the door number (1/2/3)"))
door=[1,2,3]
computer_choice=random.choice(door)
if computer_choice==participant_choice:
    change=input("is it to your advantage to switch your choice(yes/no)")
    if change=='yes':
        new_choice=input("Choose another door")
        if new_choice==computer_choice:
            print("You won the car")
        else:
            print(f"In door there is a goat and you lose")
    else:
        print("You won the  car")
else:
    change=input("is it to your advantage to switch your choice(yes/no)")
    if change=='yes':
        new_choice=input("Choose another door")
        if new_choice==computer_choice:
            print("You won the car")
        else:
            print(f"In the door {new_choice} there is a goat and you lose")
    else:
        print("You lose")
