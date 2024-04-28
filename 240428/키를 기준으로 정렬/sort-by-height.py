n = int(input())

class person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []

for i in range(n):
    name, height, weight = input().split()
    people.append(person(name, height, weight))

people.sort(key=lambda x : x.height)

for person in people:
    print(f"{person.name} {person.height} {person.weight}")