n, m, k = tuple(map(int, input().split()))

arr = [0]*(n+1)

for _ in range(m):
    num = int(input())

    arr[num] +=1

ans = -1

for i,num in enumerate(arr):
    if num>=k:
        ans = i
        print(ans)

if ans==-1:
    print(ans)