import random

item_list = ["Rock","Paper","Scissor"]
user_choice = input("Enter your move here (Rock,Paper,Scissor) =")

comp_choice = random.choice (item_list)

print(f"You choose = {user_choice}: Computer choose = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same : Match Tie!")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Computer win!")
    else :
        print("You win!")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("You win!")
    else:
        print("Computer win!")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Computer win!")
    else :
        print("You win!")
