import random
def guess():
    x = random.randint(0,100)
    count = 0
    try:
        while True:
            a = int(input('enter number: '))
            if a < x:
                print('try again, number too low')
                count += 1
            elif a > x:
                print('try again, number too high')
                count += 1
            else:
                print('CONGRATULATIONS, YOU ARE CORRECT')
                print(f'You guess it in {count} chances')
                break
    except Exception as e:
        print(f'enter a number! {e}')

guess()