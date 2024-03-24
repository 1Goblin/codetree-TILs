arr = list(map(int, input().split()))
cnt = 0
s = 0
for i in arr:
    cnt+=1
    if i==0:
        for k in range(cnt-2,cnt-5,-1):
            s+=arr[k]
        break
        
print(s)