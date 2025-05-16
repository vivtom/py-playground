def factoriall(n):
    a = 1
    for i in range(1,n+1):
        a = a * i 
    print(a)
n = int(input('enter number'))
factoriall(n)
        