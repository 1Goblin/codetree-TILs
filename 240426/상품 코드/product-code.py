class product:
    def __init__(self, name, code):
        self.na = name
        self.co = code

name, code = input().split()

p1 = product("codetree", 50)

p2 = product(name, code)

print(f"product {p1.co} is {p1.na}")
print(f"product {p2.co} is {p2.na}")