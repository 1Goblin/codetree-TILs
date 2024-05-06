n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = [0]*100

for x1, x2 in arr:


    for i in range(x1, x2+1):
        ans[i] +=1


print(max(ans))