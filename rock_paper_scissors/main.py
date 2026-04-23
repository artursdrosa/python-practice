from game import game

try:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
except ValueError:
    print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

if choice in ['rock', 'paper', 'scissors']:
    print(game(choice))
else:
    print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")