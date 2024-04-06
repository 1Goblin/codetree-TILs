n = int(input())
num=1

arr2 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

if n%2==0:
    for i in range(n-1,-1,-1):
        if i%2==1:
            for j in range(n-1,-1,-1):
                arr2[j][i]=num
                num+=1
        else:
            for j in range(n):
                arr2[j][i]=num
                num+=1
else:
    for i in range(n-1,-1,-1):
        if i%2==0:
            for j in range(n-1,-1,-1):
                arr2[j][i]=num
                num+=1
        else:
            for j in range(n):
                arr2[j][i]=num
                num+=1

for row in arr2:
    for i in row:
        print(i,end=" ")
    print()