n = input()

n = list(n)

for i in range(len(n)):
    if n[i]=="e":
        n.pop(i)
        break
n = "".join(n)
print(n)