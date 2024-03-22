arr = input().split()

s = int(arr[0])
e = int(arr[1])
cnt = 0

for i in range(s,e+1):
    s = 0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        cnt+=1
    
print(cnt)