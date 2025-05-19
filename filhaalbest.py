player = None
a=b=c=d=e=f=g=h=i = None
# n = 0 to stop when no one ones
def game():
    
    # global n  to stop when no one ones
    # while n <= 9:     to stop when no one ones
        player_O()
        player_X()
        n += 1
        win(a,b,c,d,e,f,g,h,i)
    
def player_O():
    print("player O's turn")
    global player
    player = 'O'
    where()
    
  

def where():
    r = int(input('enter row'))
    co = int(input('enter column'))
    if r != None and co != None:
        print('already taken, choose another values')
    where()
    print(f'you row value was: {r}')
    print(f'you column value was: {co}')
    put_mark_on_board(r,co)


def put_mark_on_board(r,co):
    global a,b,c,d,e,f,g,h,i
    
    if r == 1 and co == 1:
        a = player
    elif r == 1 and co == 2:
        b = player
    elif r == 1 and co == 3:
        c = player
    elif r == 2 and co == 1:
        d = player
    elif r == 2 and co == 2:
        e = player
    elif r == 2 and co == 3:
        f = player
    elif r == 3 and co == 1:
        g = player
    elif r == 3 and co == 2:
        h = player
    elif r == 3 and co == 3:
        i = player
    visual(a,b,c,d,e,f,g,h,i)

def visual(a,b,c,d,e,f,g,h,i):
    print('------+------+------')
    print(f' {a}  | {b}  | {c} ')
    print('------+------+------')
    print(f' {d}  | {e}  | {f} ')
    print('------+------+------')
    print(f' {g}  | {h}  | {i} ')
    print('------+------+------')
    
    

def player_X():
    print('X turn')
    global player
    player = 'X'
    where()


def win(a,b,c,d,e,f,g,h,i):
    if (a == 'O' and b == 'O' and c == 'O') or (d == 'O' and e == 'O' and f == 'O') or (g == 'O' and h == 'O' and i == 'O') or (a == 'O' and d == 'O' and g == 'O') or (b == 'O' and e == 'O' and h == 'O') or (c == 'O' and f == 'O' and i == 'O') or (a == 'O' and e == 'O' and i == 'O') or (c == 'O' and e == 'O' and g == 'O'):
        print('O won!')

    elif (a == 'X' and b == 'X' and c == 'X') or (d == 'X' and e == 'X' and f == 'X') or (g == 'X' and h == 'X' and i == 'X') or (a == 'X' and d == 'X' and g == 'X') or (b == 'X' and e == 'X' and h == 'X') or (c == 'X' and f == 'X' and i == 'X') or (a == 'X' and e == 'X' and i == 'X') or (c == 'X' and e == 'X' and g == 'X'):
        print('X won!')

    else: 
        game()

game()