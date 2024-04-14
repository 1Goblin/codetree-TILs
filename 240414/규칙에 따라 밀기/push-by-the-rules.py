n = input()
c = input()


for i in c:
    if i=="L":
        n = n[1:] + n[0]
    elif i=="R":
        n = n[-1] + n[:-1]
print(n)