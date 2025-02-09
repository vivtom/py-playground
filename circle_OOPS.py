class Circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(3.14159265359 * (self.radius ** 2))
    def parameter(self):
        print(2 * 3.14159265359 * self.radius)
circle1 = Circle(5)
print('Your radius :', circle1.radius)

print('Area : ', end='')
circle1.area()
print('Parameter : ' ,end='')
circle1.parameter()