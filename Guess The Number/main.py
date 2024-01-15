import os

import random

from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

attempts = 0
def check_answer(guess, answer, attempts):
    """Check answer against guess. Returns the number of remaining attempts."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower() == 'hard':
        return HARD_LEVEL_ATTEMPTS
    elif level.lower() == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return 5

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)

    attempts = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

play_game()

restart = True
while restart:
    if input("Play again? 'yes' or 'no': ").lower() == 'no':
        restart = False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        play_game()