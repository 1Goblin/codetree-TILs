class person:
    def __init__(self, name, num, area):
        self.name = name
        self.num = num
        self.area = area

n = int(input())

arr = []

max_name=""
pera = 0
for i in range(n):
    name, num, area = input().split()
    arr.append(person(name, num, area))
    if max_name<name:
        max_name = name
        pera = i
        


print(f"name {arr[pera].name}")
print(f"addr {arr[pera].num}")
print(f"city {arr[pera].area}")