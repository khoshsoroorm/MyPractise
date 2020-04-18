class School:
    def __init__(self):
        student_age = 0
        student_height = 0
        student_weight = 0
        a = input()
        h = input()
        w = input()
        a = a.strip().split()
        for i in range(len(a)):
            student_age += int(a[i])
        h = h.strip().split()
        for i in range(len(h)):
            student_height = int(h[i]) + student_height
        w = w.strip().split()
        for i in range(len(w)):
            student_weight = int(w[i]) + student_weight
        self.age = student_age
        self.weight = student_weight
        self.height = student_height

    def bmi(self,n):
        print((self.age)/n)


n = input()
classA = School()
print(classA.age)
classA.bmi(n)