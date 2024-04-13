n = input()

print(n)
for i in range(len(n)):
    n = n[-1] + n[:-1]
    print(n)