class Student():
    def __init__ (self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        total_average = (self.marks1 + self.marks2 + self.marks3)/3
        print(self.name , total_average)

s1 = Student('VIVEK', 90 ,98, 95)
s1.average()



#Using loop for marks 
class Student():
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for i in self.marks:
            sum += i 
        print(sum/len(self.marks))
s1 = Student('VIVEK', [30,60,90,53])
s1.average()
