arr = list(map(int, input().split()))
na = [0]*11


for i in arr:
    if i==0:
        break
    na[i//10]+=1

for k in range(10,0,-1):
    print(f"{k*10} - {na[k]}")