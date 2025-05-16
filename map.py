''' Use map to convert all input to int in one go. It should throw error if someone tries to enter any other data type than integer '''

a,b,c = map(int,input('enter 3 numbers').split())
print(a)

''' one more example '''
a = input('enter').split()
set1 = set()
set1.update(map(int,a))
print(set1)