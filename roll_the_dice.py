import random
def dice():
    while True:
        x = input('Roll the dice? y/n: ')
        if x == 'y':
            num = 0
            a,b = (random.randint(1,6),random.randint(1,6))

            ''' Was doing this earlier, but it increases time complexity
            for i in range(2):
                num = random.randint(1,6)
                print(num, end='') '''
        
            print(a,b)
        elif x == 'n':
            print('thanks for playing')
            break
        else:
            print('invalid')


dice()
        