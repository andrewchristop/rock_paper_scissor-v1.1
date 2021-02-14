#Program created by Christopher Andrew from scratch (13/12/2021)
#Version 1.1
#This code is open source, feel free to use my work, don't forget to add proper credits
#Enjoy!
import random
def main():
    outcomes = ["rock", "paper", "scissor"]
    #suggested_inputs = ["rock" , "paper", "scissor"]
    comp_response = [" Better luck next time, pal", " Ouch, that must've hurt", " Humans will never beat us", " Cry more", " Stay Triggered"]
    user_response = [" It's gonna be a cold day in hell before you ever get to beat us", " Time to celebrate", " There won't be a next round" ]
    user_input = input("Please make a move: ")
    comp_move = random.choice(outcomes)
    response = random.choice(comp_response)
    response_1 = random.choice(user_response)    
    if user_input in outcomes:
        if comp_move == "rock" and user_input == "scissor":
            print("Computer picks: "+ comp_move)
            print("You lost!" + response)
        elif comp_move == "paper" and user_input == "rock":
            print("Computer picks: "+ comp_move)
            print("You lost!" + response)
        elif comp_move == "scissor" and user_input == "paper":
            print("Computer picks: "+ comp_move)
            print("You lost!" + response)
        elif comp_move == user_input:
            print("Computer picks: "+ comp_move)
            print("It's a draw!")
        else:
            print("Computer picks: "+ comp_move)
            print("I win!" + response_1)
    else:
        print("Please enter a valid move")
        main()
    
    print()
    while True:
        ques = input("Would you like to have another go (y/n)?: ").lower()
        if ques == "y":
            main()
        elif ques == "n":
            exit()
        else:
            print("Please enter a valid input")        
    

main()
    
    
