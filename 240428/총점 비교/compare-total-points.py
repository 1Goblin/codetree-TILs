n = int(input())

class student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


students = []

for i in range(n):
    name, kor, eng, math = input().split()

    students.append(student(name, int(kor), int(eng), int(math)))

students.sort(key=lambda x: x.kor + x.eng + x.math)

for student in students:
    print(student.name, student.kor, student.eng, student.math)