import sys

x, y = tuple(map(int, input().split()))


max_c = -sys.maxsize

for i in range(x, y+1):
    cnt = 0
    while (1):
        if i<=0:
            break
        cnt+=i%10
        i = i//10
    
    max_c = max(max_c, cnt)

print(max_c)