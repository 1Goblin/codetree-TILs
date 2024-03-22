arr = input().split()

s = int(arr[0])
e = int(arr[1])
c = 0

for i in range(s, e+1):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==3:
        c+=1
    

print(c)