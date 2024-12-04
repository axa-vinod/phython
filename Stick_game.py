"""
Aksa Vinod
03-12-2024
"""
def stick_game():
    print("Welcome to stick game")
    print("Rules: You can only pick 1/2/3 sticks at a time ")
    print("The player who take last stick will lose the game")
    player1=input("Enter the name of first player")
    player2=input("Enter he name of second player")
    no_of_sticks=16
    while True:
        choice1=int(input(f" {player1}:Enter the no of sticks to be picked (1/2/3)"))
        if choice1>3 or choice1>no_of_sticks:
            print(f"{player1}You break the rules")
            continue
        no_of_sticks = no_of_sticks - choice1
        print("The sticks remaining is ",no_of_sticks)
        if no_of_sticks==0:
            print(f"{player1} You lose")
        choice2=int(input(f"{player2 }: Enter the no of sticks to be picked (1/2/3)"))
        if choice2>3 or choice2>no_of_sticks:
            print(f"{player2} You break the rules")
            continue
        no_of_sticks = no_of_sticks - choice2
        print("The remaining sticks is" , no_of_sticks)
        if no_of_sticks==0:
            print(f"{player2} You lose")
            break
stick_game()