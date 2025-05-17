''' GAME - GUESS THE NUMBER. 

Added multiple features :
1- A feature of allowing the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level.
2- A feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed. 
3- A feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game. '''

import random
def guess():
    print('''NOTE : YOU HAVE LIMITED CHANCES.\nEnter the range you want to play. The higher the range, the more difficult it will be.''')
    low = int(input('From? (enter a valid number): '))
    high = int(input('to? (enter a valid number): '))
    x = random.randint(low,high)
    count = 1
    best_score = float('inf')
    try:
        while True:
            a = int(input('Guess a number: '))
            if count == 10:
                print(f'You lose! The number was {x} ')
                best_score = min(count,best_score)
                print(f'Your best score is {best_score}')
                break
            elif a < x:
                print('try again, number too low')
                count += 1
            elif a > x:
                print('try again, number too high')
                count += 1
            else:
                print('CONGRATULATIONS, YOU ARE CORRECT')
                print(f'You guessed it in {count} chances')
                best_score = min(count,best_score)
                print(f'Your best score is {best_score}')
                break
    except Exception as e:
        print(f'enter a number! {e}')

guess()