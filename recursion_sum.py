''' Sum it up all the way till n '''

def sum_it(n):
    if n == 1:
        return 1 
    elif n == 0:
        return 0
    else:
        return sum_it(n-1) + n 
print(sum_it(0))
    