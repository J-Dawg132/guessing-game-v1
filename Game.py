import random

record = 0
players_guess = int(input('Choose a number(Between 0-5):\n'))
computers_guess = random.randrange(0, 6)

print('You guessed: {}'.format(players_guess))
print('The computer chose: {}'.format(computers_guess))
print()

if players_guess == computers_guess:
    print('Good Job!')
    print()
else:
    print('So close')
    print()

continue_1 = input('Would you like to try again?\n')
    
while (continue_1 != 'q'): 

    players_guess = int(input('Choose a number(Between 0-5):\n'))
    computers_guess = random.randrange(0, 6)
    print('You guessed: {}'.format(players_guess))
    print('The computer chose: {}'.format(computers_guess))
    print()

    if players_guess == computers_guess:
        print('Good Job!')
        print()
        record += 1  
    else:
        print('So close')
        print()

    continue_1 = input('Would you like to try again?\n')

print()
print('Game over')
print('Your record is, {} wins'.format(record))