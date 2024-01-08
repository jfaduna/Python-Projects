import random

options = [
'''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
''',
'''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
''',
'''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
'''
]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user < 0 or user > 2: 
    print("You entered an invalid input. You lose.")
else:
    print(options[user])
    print('Computer chose:')
    computer = random.randint(0,2)
    print(options[computer])
    if user == 0 and computer == 2:
        print('You won!')
    elif user > computer:
        print('You won!')
    elif user == computer:
        print("It's a draw!")
    else:
        print(f'You lose. Try again.')