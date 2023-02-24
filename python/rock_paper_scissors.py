import random

def get_choices():  
    player_choices = input("Enter Choices => rock, paper, scissors: ")   
    options = ["rock", "paper","scissors"]
    computer_choices = random.choice(options) 
    choices = {"player": player_choices, "computer": computer_choices} 
    return choices


print_get_choices = get_choices() 
print(print_get_choices)