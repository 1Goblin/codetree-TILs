n = int(input())
arr = list(map(int, input().split()))

def fun(n):
    if n==0:
        return arr[0]
    
    return max(arr[n-1], arr[n])

print(fun(n-1))