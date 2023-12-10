import random as RD

#count the player's score
score = 0
#Set user_input to 0 to use it later in the script
user_input = 0

def fix_err(user_input):
    
    while True:
            try:
                user_input = int(input("Enter a number between 0 and 10: "))
                if user_input == 99:
                    exit()
                if 0 <= user_input <= 10:
                        return user_input
                    
                else:
                            print("Invalid input. Please enter a number between 0 and 10.")
                            
            except ValueError:
                
                        if 0 > user_input or user_input > 10:
                            print("Invalid input. Pleas enter a number betwwen [0 - 10] : ")
                        
                        print("Invalid input. Please enter a valid integer ")

print("Welcome to the game! : you might take the following in your considerations :")
print("- Enter a valid integer between 0 and 10.")
print("- Make sure to input only numbers, not characters or strings.")
print("- if you want to start a new game enter -> 1. If not perss any key in your keyboard")
print("- You are free to exit the any time you want. Just enter -> 99")
while True:
    print("New game?----------> ")
    start_game = input()
    
    if start_game == "1":
        
        generated_num = RD.randrange(0, 10)
        
        while True:
            
            user_input = fix_err(user_input)
                    
            if user_input == generated_num:
                
                score += 1
                print(f"You won the game !!!!! and your score is {score}")
                break
                
            elif user_input < generated_num:
                
                score += 1
                print("Go higher")
                
            elif user_input > generated_num:
                
                score += 1
                print("Go lower")
        
    else:
        exit()