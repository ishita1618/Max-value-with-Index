import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!"

list=["rock","paper","scissors"]
while True:
    computer_count=0
    user_count=0
    user_choice=int(input('''
Game start.....
1 Yes | Play
2 No | Exit
            '''))
    if user_choice==1:
        for i  in range(1,6):
            user_input=int(input('''
1 rock          
2 scissors      
3 paper  
            '''))
            if user_input==1:
                user_choice="rock"
            elif user_input==2:
                user_choice="scissors"
            elif user_input==3:
                user_choice="paper"
            computer_choice=random.choice(1)
            if computer_choice==user_choice:
                print("Computer Value", computer_choice)
                print("User Value", user_choice)
                print("Game Draw")
                user_count=user_count+1
                computer_count=computer_count+1
            elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="paper" and  computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper"):
                print("Computer Value", computer_choice)
                print("User Value", user_choice)
                print("You Win")
                user_count = user_count + 1
            else:
                print("Computer Value", computer_choice)
                print("User Value", user_choice)
                print("Computer Win")
                computer_count = computer_count + 1

        if user_count==computer_count:
            print("Final Game Draw....")
            print("User Score", user_count)
            print("Computer Score", computer_count)
        elif user_count>computer_count:
            print("You Win The Game....")
            print("User Score", user_count)
            print("Computer Score", computer_count)
        else:
            print("Computer Win The Game....")
            print("User Score", user_count)
            print("Computer Score", computer_count)

    else:
        break
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")