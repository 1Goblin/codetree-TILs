n = int(input())
cows_h = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cows_h[i] <= cows_h[j] and cows_h[j] <= cows_h[k]:
                cnt+=1

print(cnt)