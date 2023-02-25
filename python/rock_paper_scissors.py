import random

def get_choices():  
    player_choices = input("Enter Choices => rock, paper, scissors: ")   
    options = ["rock", "paper","scissors"]
    computer_choices = random.choice(options) 
    choices = {"player": player_choices, "computer": computer_choices} 
    print("--------------")
    return choices

def check_win(player, computer): 
    print(f"you chose {player}, computer chose {computer}") 
    if player == computer: 
        return "its a tie" 
    elif player == "rock":
        if computer == "scissors": 
            return "Rock smashes scissors! You win" 
        else: 
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else: 
            return "Scissors cut paper! You lose."
    elif player == "scissors":
        if computer == "paper": 
            return "Scissors cut paper! You win!"
        else: 
            return "Rock samashes scissors! You lose." 
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"]) 
print("--------------")
print(result)
print("--------------")
           
    
   



#print_get_choices = get_choices() 
#print(print_get_choices)