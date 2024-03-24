arr = list(map(int,input().split()))
cnt = 0
sum = 0
for i in arr:
    if i==0:
        break
    sum+=i
    cnt+=1

ave = sum/cnt
print(f"{sum} {ave:.1f}")