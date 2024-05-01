n, k = tuple(map(int,input().split()))
arr = list(map(int, input().split()))

max_s = 0

for i in range(n-k+1):
    s = 0
    for j in range(i,i+k):
        s += arr[j]
    max_s = max(max_s, s)

print(max_s)