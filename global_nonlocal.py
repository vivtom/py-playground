# Define a function that uses a global variable, and another nested function inside it that modifies a nonlocal variable. Print the values before and after modification.
a = 2 
def hey():
    global a
    a = 4
    b = 5
    def hello():
        nonlocal b 
        b = 10 
    hello()
    print(b)
hey()
print(a)