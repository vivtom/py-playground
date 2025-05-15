''' print any multiplication table in reverse order'''
n = int(input('enter'))
for i in range(10,0,-1):
    print(f" {i} X {n} is {i*n}")
    