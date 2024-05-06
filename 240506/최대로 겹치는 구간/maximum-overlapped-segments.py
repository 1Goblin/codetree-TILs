n = int(input())

arr = [0]*100

for _ in range(n):
    a, b = tuple(map(int, input().split()))

    for i in range(a,b):
        arr[i] += 1
    
print(max(arr))