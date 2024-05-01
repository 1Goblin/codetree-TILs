n, k = tuple(map(int, input().split()))

d ={
    "G" : 1,
    "H" : 2,
    0 : 0
}

arr = []
max_n = 0
for i in range(n):
    p, a = input().split()
    p = int(p)
    arr.append([p,a])
    max_n = max(max_n, p)

narr = [0] * (max_n + 1)

for i in arr:
    narr[i[0]] = i[1]

max_s = 0
for i in range(1, max_n-k+1):
    s = 0
    for j in range(i, i+k+1):
        s+=d[narr[j]] 
    max_s = max(max_s, s)

print(max_s)