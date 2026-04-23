import random

def game(choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    print(f"Computer chose: {computer_choice}")

    if choice == computer_choice:
        return f"It's a tie! Both chose {choice}."
    elif (choice == 'rock' and computer_choice == 'scissors') or \
         (choice == 'paper' and computer_choice == 'rock') or \
         (choice == 'scissors' and computer_choice == 'paper'):
        return f"You win! {choice} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice} beats {choice}."