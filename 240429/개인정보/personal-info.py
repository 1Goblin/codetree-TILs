class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []
for i in range(5):
    name, height, weight = input().split()

    students.append(student(name, int(height), float(weight)))

students.sort(key=lambda x : x.name)

print("name")
for i in students:
    print(i.name, i.height, i.weight)

print()
print("height")
students.sort(key=lambda x : -x.height)

for i in students:
    print(i.name, i.height, i.weight)