n, m = tuple(map(int, input().split()))

di = {
    "L": -1,
    "R": 1
}
a = [0]
b = [0]
ap = 0
bp = 0
for _ in range(n):
    d, t = input().split()
    for i in range(int(t)):
        ap+=di[d]
        a.append(ap)

for _ in range(m):
    d, t = input().split()
    for i in range(int(t)):
        bp+=di[d]
        b.append(bp)
ans = -1

for i in range(1,len(a)):
    if a[i]==b[i]:
        ans = i
        break

print(ans)