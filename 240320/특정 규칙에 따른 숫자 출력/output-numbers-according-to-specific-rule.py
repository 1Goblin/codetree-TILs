n = int(input())
cnt=0

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        cnt+=1
        if cnt==10:
            cnt=1
        print(cnt,end=" ")
    print()