n = int(input())

class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


students = []

for i in range(n):
    name, height, weight = input().split()

    students.append(student(name, int(height), int(weight)))


students.sort(key=lambda x : (x.height, -x.weight))

for i in students:
    print(i.name, i.height, i.weight)