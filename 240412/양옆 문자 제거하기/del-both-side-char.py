n = input()

n = list(n)

n.pop(1)
n.pop(-2)

n = "".join(n)
print(n)