class School:
    def __init__(self):
        self.n = int(input())
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

    def calc_height(self):
        bmi_height = float(self.height / self.n)
        return bmi_height
    def calc_age(self):
        bmi_age = float(self.age / self.n)
        return bmi_age
    def calc_weight(self):
        bmi_weight = float(self.weight / self.n)
        return bmi_weight


classA = School()
classB = School()
print('{}'.format(classA.calc_age()))
print('{}'.format(classA.calc_height()))
print('{}'.format(classA.calc_weight()))
print('{}'.format(classB.calc_age()))
print('{}'.format(classB.calc_height()))
print('{}'.format(classB.calc_weight()))


if classA.calc_height() > classB.calc_height():
    if classA.calc_weight() > classB.calc_weight():
        print('A')
    elif classA.calc_weight()< classB.calc_weight():
        print('B')
    else:
        print('Same')
elif classA.calc_height() < classB.calc_height():
    if classA.calc_weight() < classB.calc_weight():
        print('B')
    elif classA.calc_weight() > classB.calc_weight():
        print('A')
    else:
        print('Same')
else:
    if classA.calc_weight() < classB.calc_weight():
        print('B')
    elif classA.calc_weight() > classB.calc_weight():
        print('A')
    else:
        print('Same')