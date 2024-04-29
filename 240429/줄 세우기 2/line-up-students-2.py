n = int(input())

class student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

students = []

for i in range(n):
    height, weight = map(int, input().split())

    students.append(student(height, weight, i+1))

students.sort(key=lambda x : (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.num)