import random

def guessing_game():
    number = random.randint(0, 100)
    user_num = int(input('Please guess a number from [0, 100] range: '))

    while user_num != number:
        if user_num > number:
            print(f'Your guess of {user_num} is too high!')
        else:
            print(f'Your guess of {user_num} is too low!')
        user_num = int(input('Please guess a number from [0, 100] range: '))
    
    print(f'Right!  The answer is {number}')

# guessing_game()
