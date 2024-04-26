class cha:
    def __init__(self, id=0, level=0):
        self.id = id
        self.level = level

id, level = input().split()

c1 = cha("codetree", 10)
c2 = cha()
c2.id = id
c2.level = level

print(f"user {c1.id} lv {c1.level}")
print(f"user {c2.id} lv {c2.level}")