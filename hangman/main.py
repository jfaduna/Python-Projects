import os

import random

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

game_over = False
lives = 6

chosen_word = random.choice(word_list)
print(logo)
print(f"HINT: the word is {chosen_word}")

display = ["_" for _ in chosen_word]

while not game_over:
    guess = input('\nGuess a letter: ').lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if guess in chosen_word:
        if guess not in display:
            for i in range(len(chosen_word)):
                letter = chosen_word[i]
                if letter == guess:
                    display[i] = letter
        else:
            print(f"You've already guessed '{guess}'")
    
    print(' '.join(display))

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"Wrong guess, letter '{guess}' is not in the word. You lose a life.")
    

    if lives == 0:
        game_over = True
        print('You lose.')

    if "_" not in display:
        game_over = True
        print(f'The word is {chosen_word}. You win.')
    

