import random
import sys

RPS_list = ["p", "r", "s"]

print("Paper == p\nScissor == s\nRock == r")

def get_user_input():
    user_input = input("Choose what to play with: ").lower()
    
    while user_input not in RPS_list:
    
        print("Invalid input. Please enter 'r', 'p', or 's'.")    
        user_input = input("Choose what to play with: ").lower()
    
    return user_input

users_input = get_user_input()

#choose a random element from the list (rock) (peper) (scissor)
PCs_input = random.choice(RPS_list)
print("the pc chose ",PCs_input)

if users_input == PCs_input:
    print("Tie!!!!!!")
elif (users_input == "p" and PCs_input == "r") or (users_input == "r" and PCs_input == "s") or (users_input == "s" and PCs_input == "p"):
    print("You Won!!")
else:
    print("You lost")