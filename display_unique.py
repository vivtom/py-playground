# take input from user and show the unique ones
a = input('enter 8 numbers').split()
set1 = set()

set1.update(map(int, a))
print(list(set1))