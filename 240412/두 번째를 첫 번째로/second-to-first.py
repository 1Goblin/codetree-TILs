n = input()

n = list(n)

c = n[1]


for i in range(len(n)):
    if n[i]==c:
        n[i]=n[0]

n = "".join(n)
print(n)