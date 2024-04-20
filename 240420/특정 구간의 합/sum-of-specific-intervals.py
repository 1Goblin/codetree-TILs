n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def add(a, b):
    cnt = 0
    for i in range(a-1,b):
        cnt+=arr[i]
    
    return cnt


for i in range(m):
    a, b = map(int, input().split())
    print(add(a, b))