arr = list(map(int,input().split()))
na = [0]*10

for i in arr:
    if i==0:
        break
    for j in range(1,10):
        if i//10 == j:
            na[j] +=1

for k in range(1,10):
    print(f"{k} - {na[k]}")