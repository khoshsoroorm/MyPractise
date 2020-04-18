class Person:
    count = 0

    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age
        print(self.age,self.weight,self.height)

    def bmi(self):
        print(sum(self.age)/n)
        print(sum(self.height)/n)
        print(sum(self.age)/n)


def input_list():

i = 1
while i <= 2:
    n = int(input())
    student_age = []
    student_height = []
    student_weight = []
    for i in range(0, n):
        s = int(input())
        student_age.append(s)
    for i in range(0,n):
        h = int(input())
        student_height.append(h)
    for i in range(0,n):
        w = int(input())
        student_weight.append(w)

    student = Person(student_height, student_weight, student_age)
    BMI = student.bmi()

    i+=1
