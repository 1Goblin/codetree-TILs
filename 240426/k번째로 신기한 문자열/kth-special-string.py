n, k, T = input().split()
n = int(n)
k = int(k)

arr = [
    input()
    for _ in range(n)
]

na = []

for i in arr:
    if i[:len(T)]==T:
        na.append(i)

na.sort()

print(na[k-1])