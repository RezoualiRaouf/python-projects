import random
import sys

RPS_list = ["p", "r", "s"]

print("Peper == p \nScissor == s\nRock == r")

users_input = str(input("choose  what to play with "))

#check if the user entered the right input (r, p, s) and exite if it is.
if users_input not in RPS_list:
    print("Invalid input. Please enter 'r' 'p' or 's'.")
    sys.exit(1)
        
#choose a random element from the list (rock) (peper) (scissor)
PCs_input = random.choice(RPS_list)
print("the pc chose ",PCs_input)

if users_input == PCs_input:
    print("Tie!!!!!!")
elif (users_input == "p" and PCs_input == "r") or (users_input == "r" and PCs_input == "s") or (users_input == "s" and PCs_input == "p"):
    print("You Won!!")
elif (users_input == "r" and PCs_input == "p") or (users_input == "s" and PCs_input == "r") or (users_input == "p" and PCs_input == "s"):
    print("You lost") 