"""
Winning Rule as Follows:
Rock vs paper -> paper wins
Rock vs scissor -> Rock wins
paper vs scissor -> scissor wins
"""

import random

l = ["rock","paper","scissor"]

while True:
    computer_count = 0
    user_count = 0

    user_choice = int(input("""
Game start.....
1 Yes
2 No | Exit
                    """))
    
    
    if user_choice == 1:
        for i in range(1,6):
            user_input = int(input("""
1 Rock
2 Scissor
3 Paper
            """))
            
            if user_input == 1:
                user_choice = "rock"
            elif user_input == 2:
                user_choice = "scissor"
            elif user_input == 3:
                user_choice = "paper"
            computer_choice = random.choice(l)
            
            if computer_choice == user_choice:
                print("Computer value", computer_choice)
                print("User value", user_choice)
                print("Game Draw")
                computer_count +=1
                user_count +=1
            elif(user_choice=="rock" and computer_choice=="scissor") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissor" and computer_choice=="paper"):
                print("Computer value", computer_choice)
                print("User value", user_choice)
                print("You win")
                user_count +=1
            else:
                print("Computer value", computer_choice)
                print("User value", user_choice)
                print("Coumputer win")
                computer_count +=1
                
        if user_count == computer_count:
            print("Final Game Draw.....")
            print("User Count",user_count)
            print("Computer Count",computer_count)
        elif user_count > computer_count:
            print("Final You WIN The Game.....")
            print("User Count",user_count)
            print("Computer Count",computer_count)
        else:
            print("Final Computer WIN The Game.....")
            print("User Count",user_count)
            print("Computer Count",computer_count)

    else:
        break
