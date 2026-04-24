def guess_the_number(guess, number_to_guess):
    while not guess:        
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            exit()


        if user_guess < 1 or user_guess > 100:
            print("Please guess a number between 1 and 100.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guess = True
            print(f"Congratulations! You've guessed the number! It's {number_to_guess}.")
            return