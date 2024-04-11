n = input()

n = list(n)

a = n[0]
b = n[1]

for i in range(len(n)):
    if n[i]==a:
        n[i]=b
    elif n[i]==b:
        n[i]=a
n = "".join(n)

print(n)