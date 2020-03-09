# Write your code here
import random
comp_options = ['rock', 'paper', 'scissors']


while(True):
    comp_guess = random.choice(comp_options)
    guess = input()
    if guess == comp_guess:
        print(f'There is a draw ({comp_guess})')
    elif guess == 'rock' and comp_guess == 'paper':
        print(f'Sorry, but computer chose {comp_guess}')
    elif guess == 'rock' and comp_guess == 'scissors':
        print(f'Well done. Computer chose {comp_guess} and failed')
    elif guess == 'paper' and comp_guess == 'scissors':
        print(f'Sorry, but computer chose {comp_guess}')
    elif guess == 'paper' and comp_guess == 'rock':
        print(f'Well done. Computer chose {comp_guess} and failed')
    elif guess == 'scissors' and comp_guess == 'rock':
        print(f'Sorry, but computer chose {comp_guess}')
    elif guess == 'scissors' and comp_guess == 'paper':
        print(f'Well done. Computer chose {comp_guess} and failed')
    elif guess == '!exit':
        print('Bye!')
        break
