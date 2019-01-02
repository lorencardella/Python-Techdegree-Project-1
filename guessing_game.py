"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
# Thank you for viewing my assignment.  Please reject it if it earns less than an "exceeds expectations" grade.

import random


def start_game():
    print("This is a number-guessing game.  It randomly generates a number between 1 and 10 for you to guess.")
    correct_number = random.randint(1, 10)
    current_guess = -1
    total_guesses = 1
    correct_guess = False
    best_round = 65535
    done_playing = False
    
    while done_playing == False:

        while correct_guess == False:
            try:
                current_guess = int(input("What is your guess? "))
            except ValueError:
                print("That isn't valid as a guess.  Please try again.")
                continue
            if current_guess > 10 or current_guess < 1:
                print("Please guess between 1 and 10.")
                continue
            if current_guess == correct_number and total_guesses == 1:
                correct_guess = True
                print("Got it.  You correctly guessed", correct_number, "on your first try.  This is the best possible result.  Thank you for playing.")
                answer = "no"
                done_playing = True
            elif current_guess == correct_number and total_guesses > 1:
                correct_guess = True
                print("Got it.  You correctly guessed", correct_number, "in", total_guesses, "tries.")
                break
            elif current_guess > correct_number:
                total_guesses += 1
                print("It's lower.")
                continue
            elif current_guess < correct_number:
                total_guesses += 1
                print("It's higher.")
                continue
                
        if total_guesses < best_round:
            best_round = total_guesses
            
        if best_round > 1:
            print("Your best round required", best_round, "tries.")
            answer = str(input("Would you like to try again for a better result?")).lower()
        
        if answer == "y" or answer == "yes":
            answer = "blank"
            total_guesses = 1
            correct_number = random.randint(1, 10)
            correct_guess = False
        elif answer == "n" or answer == "no":
            answer = "blank"
            print("Goodbye.")
            done_playing = True
        else:
            print("Please answer 'yes' or 'no.'")
            
            
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
