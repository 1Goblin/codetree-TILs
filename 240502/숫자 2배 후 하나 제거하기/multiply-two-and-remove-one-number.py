import sys

n = int(input())
arr = list(map(int ,input().split()))

def asum():
    s = 0
    for i in range(1,len(n_arr)):
        s+= abs(n_arr[i]-n_arr[i-1])
    return s
    

min_as = sys.maxsize

for i in range(n):
    n_arr = []
    arr[i] = arr[i]*2
    
    for j in range(n):
        n_arr = []
        for k in range(n):
            if j==k:
                continue
            n_arr.append(arr[k])

        min_as = min(min_as, asum())
    arr[i] = arr[i]//2

print(min_as)