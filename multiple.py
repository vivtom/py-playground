''' Given an interger n, print its first 10 multiples'''
if __name__ == '__main__':
    n = int(input().strip())
for i in range(1,11):
    res = n * i
    print(n, 'x', i, '=' ,res)