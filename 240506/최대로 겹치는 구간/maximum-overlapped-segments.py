n = int(input())

arr = [0]*200

for _ in range(n):
    a, b = tuple(map(int, input().split()))
    a+=100
    b+=100
    for i in range(a,b):
        arr[i] += 1
    
print(max(arr))