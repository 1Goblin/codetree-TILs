n, m, k = tuple(map(int, input().split()))

arr = [0]*(n+1)

ans = -1

for _ in range(m):
    num = int(input())
    arr[num] +=1
    if arr[num]>=k:
        print(num)
        ans = 1
        break

if ans==-1:
    print(-1)