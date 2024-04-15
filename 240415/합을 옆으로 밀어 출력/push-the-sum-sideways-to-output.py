n = int(input())

p = 0

for i in range(n):
    c = int(input())
    p+=c

p = str(p)

print(p[1:]+p[0])